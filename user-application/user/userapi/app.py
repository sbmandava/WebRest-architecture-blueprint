## Variables.
version=0.14
sql_db = 'data/user.db'

## ---- no code changes below this line ##
import os
import sys
import argparse
import models

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/user/list', methods=['GET'])
def get_users():
    result = models.list_users(sql_db)
    return jsonify(result)

@app.route('/api/v1.0/user/listuser/<userid>', methods=['GET','POST'])
def get_user(userid):
    result = models.list_user(sql_db,userid)
    return jsonify(result)


# def add_user (db_name,userID,userName,userEmail,userPhone):

@app.route('/api/v1.0/user/add/<userid>/<name>/<email>/<phone>', methods=['GET','POST'])
def add_user(userid,name,email,phone):
     result = models.add_user(sql_db,userid,name,email,phone)
     return jsonify(result)

#    try:
#       result = models.add_user(sql_db,userid,name,email,phone)
#       return jsonify("Response : 200")
#    except: # catch *all* exceptions
#        e = sys.exc_info()[0]
#        return ( "Error: %s" % e )

    # return "userid : %s name : %s email : %s phone : %s " % (userid, name, email, phone)
    # return (userid, name)
    # result = models.list_user(sql_db,userid)
    # return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False)
