# entry_management_app
* This app is used to create entries of visitors.
* It captures the Name, email address, phone no of the visitor and the host on the front end. 
* At the back end, once the user enters the information in the form, the backend stores all of
the information with time stamp of the entry and notifies the host about the visit via email and a similar notification is sent to the visitor when he/she leaves/checks out.

## Dependecies
* python3
* pip
* django

## Build and Run
### Clone the repository

`$ git clone https://github.com/mnv936/entry_management_app.git`

`$ cd entry_management_app.git`

`$ python3 manage.py makemigrations`

`$ python3 manage.py migrate`

### Add email and password
* since the app has to send emails, host user details must be mentioned 
* django.core.mail module is used to send mails using SMTP backend
* Go to entry_management_app/settings.py and change the EMAIL_HOST_USER  to your gmail id and EMAIL_HOST_PASSWORD to your email's password.
* Turn the less secure apps(https://support.google.com/accounts/answer/6010255?hl=en) option to 'on' in your google account settings.
### Start the backend server

`$ python3 manage.py runserver`

### Open browser
* Copy the link provided after giving the runserver command and open the link in a browser
* Two option are provide, one for check_in and other for check-out
* Selcting the check-in option takes you two a new page which has form a which the visitor needs to fill.
* When visitor submits the form after filling the required details
  * Visitor submitted data is stored in the database
  * An email is sent to the host containg the details of the visitor
  * Redireccted back to home page.
* Selecting the check-out option will take you to a new page which has a form, which when the visitor submits the check-out time will be added to his entry in the database.An email is also sent to the visitor containing the summary of the visit.

### Database
* To view the database, first create a superuser by the following command 
  * `$ python3 manage.py createsuperuser`
* Go to localhost:8000/admin to login and view the stored visitor objects.
