## Version
## 0.4 : Now it supports variables.
## 0.5 : Has listusers function.
## 0.6 : Add Twitter BootStrap Templates.
##        https://pythonhosted.org/Flask-Bootstrap/basic-usage.html
##


## Variables.


## ---- no code changes below this line ##
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_restful import reqparse
from flask_bootstrap import Bootstrap

from webapp.adduser_form import AddUserForm 
import requests
import json



# Create app
app = Flask(__name__)
app.config.from_object(__name__)
Bootstrap(app)
app.secret_key = 'SuperSecret key'

# Handle Routes
# Read the variable userid from url and create the REST url

@app.route('/user/listuser/<userid>', methods=['GET','POST'])
def get_user(userid):

   url = ('http://127.0.0.1:5000/api/v1.0/user/listuser/%s' % userid)

   # get request
   r = requests.get(url)

   # read it using json
   data = r.json()

   #print the first record
   # print (data[0])

   # Now let's store the data from first record.
   eMail = (data[0]['email'])
   pHone = (data[0]['phone'])
   userID = (data[0]['userid'])
   userName = (data[0]['username'])

   # return render_template('show_user.html', data = data )
   # print (eMail,pHone,userID,userName)
   return render_template('bp_show_user.html', eMail = eMail, pHone = pHone, userID = userID, userName = userName )


@app.route('/', methods=['GET','POST'])
@app.route('/user/listusers', methods=['GET','POST'])
def get_users():

   url = ('http://127.0.0.1:5000/api/v1.0/user/list')

   # get request
   r = requests.get(url)

   # read it using json
   data = r.json()

   #print the first record
   # print (data[0])

   return render_template('bp_list_users.html', data = data)

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()

   if request.method == 'POST':
       if form.validate() == False:
           flash('All fields are required.')
           return render_template('contact.html', form = form)
       else:
           return render_template('success.html')
   elif request.method == 'GET':
       return render_template('contact.html', form = form)

@app.route('/adduser', methods = ['GET', 'POST'])
def adduser():
   form = AddUserForm()

   if request.method == 'POST':
       if form.validate() == False:
           flash('All fields are required.')
           return render_template('adduser.html', form = form)
       else:
           return render_template('success.html')
   elif request.method == 'GET':
       return render_template('adduser.html', form = form)


# Now run the Server on port 8080
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
