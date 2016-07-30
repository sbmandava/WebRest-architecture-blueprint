## Variables.
version=0.14
sql_db = 'data/user.db'

## ---- no code changes below this line ##
import os
import sys
import user.userapi.models as User
import requests

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1.0/user/list', methods=['GET'])
def get_users():
    result = User.list_users(sql_db)
    return jsonify(result)

@app.route('/api/v1.0/user/listuser/<userid>', methods=['GET','POST'])
def get_user(userid):
    result = User.list_user(sql_db,userid)
    return jsonify(result)

@app.route('/api/v1.0/user/adduser', methods=['POST'])
def add_user():
    if request.method == "POST":
        json_dict = request.get_json()
        userid = json_dict['userID']
        name = json_dict['userName']
        email = json_dict['eMail']
        phone = json_dict['pHone']
        
        result = User.add_user(sql_db,userid,name,email,phone)
        return jsonify(result)
    else:
        return """<html><body>
        Something went horribly wrong
        </body></html>"""

if __name__ == '__main__':
    app.run(debug=False)
