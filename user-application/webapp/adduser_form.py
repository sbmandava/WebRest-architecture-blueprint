from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError

class AddUserForm(Form):
   userID = TextField("User ID",[validators.Required("Please enter userid.")])
   userName = TextField("User Name",[validators.Required("Please enter user name.")])
   eMail = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   pHone = IntegerField("Phone",[validators.Required("Please enter valid phone number.")])
   submit = SubmitField("Send")
