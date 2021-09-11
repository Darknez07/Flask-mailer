# Flask-mailer
* This is the task of creating an API for scheduling mails
* Celery container has called "CELERY BEAT SCHEDULER" which does not work with windows
# My approach
* I created the 5 routes
* JWT tokens
* View alerts need login
* Create user
* For each of those users we provide token
* Token is valid for 20 mins
* Token create alert queries are stored
#### Following diagram explains clearly
![Routes](SS/Routes.jpg 'Explaination of approach')
#### Tables are as follows
* Foriegn key is username
![Tables](SS/Tables.PNG 'Tables')
## Run the Code
#### Just do pip install -r requirements.txt

## When running celery
* Celery helps to divide the work
* Assign lot of workers
* We need RabbitMQ with "management protocol" enabled
#### Using then command
* celery -A app.celery worker -l INFO
![Celery](SS/Celery.PNG 'Celery')
## Note running celery as well as app on different terminals
* python app.py
* Runs on debug mode
![Terminal](SS/Pic8.PNG 'App.py')
### Most importantly It has 5 routes
#### First create/users
#### Second alerts/create
#### Third alerts/delete
#### Fourth view/alerts
#### Fifth /auth
#### and then python app.py
#### Also  will run celery clusters

* Auth is for authentication token
### Used JWT tokens and expires after 20 minutes
* Need to create user first then access the token
* Screen Shots here
![First_ss](SS/Pic6.png 'User creation')
* Using postman for authentication token
![Second](SS/Pic5.png 'Authentication')
* A view of Authenticated token
![Third](SS/Pic4.png 'Authentication')
* We need to sign in
![Mid](SS/For_alerts.PNG 'Authenticate to view')
* Then viewing the alerts
![Fourth](SS/Pic1.png 'Viewing alerts')
* Then for creating alerts
* First trying without token is futile
![Fifth](SS/Pic7.png 'Creating alerts')
* Adding token for the creating
![Sixth](SS/Add_token.PNG 'Token for authentication')
* Finally After token
![Seventh](SS/Submit_query.PNG 'Submit the create alert')
* Then coming to delete alert
![Eigth](SS/Delete_query.PNG 'Submit the create alert')