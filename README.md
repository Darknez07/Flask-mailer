# Flask-mailer
* This is the task of creating an API for scheduling mails
* Celery container has called "CELERY BEAT SCHEDULER" which does not work with windows
### Most importantly It has 5 routes
#### First create/users
#### Second alerts/create
#### Third alerts/delete
#### Fourth view/alerts
#### Fifth /auth


* Auth is for authentication token
* Used JWT tokens and expires after 20 minutes
* Need to create user first then access the token
* Screen Shots here
![First_ss](Pic6.png 'User creation')
* Using postman for authentication token
![Second](Pic5.png 'Authentication')
* A view of Authenticated token
![Third](Pic4.png 'Authentication')
* Then viewing the alerts
![Fourth](Pic1.png 'Viewing alerts')
* Then for For creating alerts
![Fifth](Pic7.png 'Create alerts')