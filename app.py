from flask import Flask, request, jsonify, make_response, render_template
import jwt
import datetime
from functools import wraps
from Users import access_database, get_list
import bcrypt


app = Flask(__name__)
app.config["SECRET_KEY"] = "First app"


def token_request(r):
    @wraps(r)
    def verify(*args, **kwargs):
        try:
            token = request.headers["Authorization"].split(" ")[-1]
        except:
            return jsonify({"message": "Please pass the token"}), 403
        try:
            jwt.decode(token, app.config["SECRET_KEY"], algorithms="HS256")
        except:
            return jsonify({"message": "Invalid token"}), 403
        return r(*args, **kwargs)

    return verify


@app.route("/alerts/create", methods=["POST", "GET"])
@token_request
def create_alerts():
    if request.method == "GET":
        return render_template("select_alert.html", lst=get_list())
    else:
        price = request.form["price"]
        try:
            price = float(price)
        except:
            return jsonify({"message": "Invalid price"}), 401
        currency = request.form["currency"]
        db = access_database()
        token = request.headers["Authorization"].split(" ")[-1]
        res = db.execute(
            "select * from alerts where token_id=? and currency=?", [token, currency]
        ).fetchall()
        if not res:
            username  = db.execute('select username from users where token_id=?',[token]).fetchall()[0]['username']
            db.execute(
                "insert into alerts(price_alert, currency, token_id, username) values(?,?,?,?)",
                [price, currency, token, username],
            )
            db.commit()
            return "Alert added"
        else:
            db.execute(
                "Update alerts set price_alert=? where token_id=? and currency=?",
                [price, token, currency],
            )
            db.commit()
            return "Alert updated"
        return "Done"


@app.route("/alerts/delete", methods=["POST",'GET'])
@token_request
def delete_alerts():
    if request.method == 'GET':
        return render_template('delete_alert.html',lst=get_list())
    else:
        token = request.headers["Authorization"].split(" ")[-1]
        currency = request.form['currency']
        db = access_database()
        db.execute('delete from alerts where token_id=? and currency=?',[token,currency])
        db.commit()
        return "<h2> Deleted at {} from user updates </h2>".format(12312)


@app.route("/auth")
def create_token():

    auth = request.authorization
    db = access_database()
    res = db.execute(
        "select password from users where username=?", [auth.username]
    ).fetchall()

    if not res:
        return jsonify({"message": "Not correct pass or username"})

    if (
        auth
        and bcrypt.hashpw(auth.password.encode("ascii"), res[0]["password"])
        == res[0]["password"]
    ):
        token = jwt.encode(
            {
                "username": auth.username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=20),
            },
            app.config["SECRET_KEY"],
        )
        db.execute(
            "update users set token_id=? where username=?", [token, auth.username]
        )
        db.execute(
            "insert into alerts(token_id,username) values(?,?)", [token, auth.username]
        )
        db.commit()
        return jsonify({"token": token})

    return make_response(
        "Cloud not verify", 401, {"WWW-Authenticate": "Login required"}
    )


@app.route("/create/user", methods=["POST", "GET"])
def create_user():
    if request.method == "GET":
        return render_template("user_details.html")
    else:
        db = access_database()
        uname = request.form["username"]
        email = request.form["email"]
        passw = bcrypt.hashpw(
            request.form["password"].encode("ascii"), bcrypt.gensalt()
        )
        try:
            db.execute(
                "insert into users(username, email, password) values(?,?,?)",
                [uname, email, passw],
            )
            db.commit()
        except:
            return "Not possible"
        return "Done"


if __name__ == "__main__":
    app.run(debug=True)
