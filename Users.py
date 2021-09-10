import urllib.request as req
import json
import  sqlite3 as sql



def update(currency):
    with req.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false') as url:
        data = json.loads(url.read().decode('utf8'))
        for d in data:
            if d['id'] == currency or d['symbol'] == currency:
                return d['current_price']
    return None

def get_list():
    lst = []
    with req.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false') as url:
        data = json.loads(url.read().decode('utf8'))
        for d in data:
            lst.append((d['symbol'], d['id']))
    return lst

def access_database():
    con = sql.connect('db/data.db')
    con.row_factory = sql.Row
    return con

def update_query(val):
    db = access_database()
    ans = db.execute('SELECT email,username,price_alert from users order by price_alert').fetchall()
    print(ans[0]['price_alert']/val)
    if ans[0]['price_alert']/val <= 1.0000012312:
        print('send email',val)
