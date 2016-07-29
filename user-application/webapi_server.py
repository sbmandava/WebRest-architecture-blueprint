## Purpose : Expose the database as a REST API functions.
## Advantages : Now 


## Variables.
version=0.14
sql_db = 'data/user.db'

## ---- no code changes below this line ##
import os
import sys
import user.userapi.models as User  # This loads user/userapi/models.py library which contains core logic.

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/user/list', methods=['GET'])
def get_users():
    result = User.list_users(sql_db)
    return jsonify(result)

@app.route('/api/v1.0/user/listuser/<userid>', methods=['GET','POST'])
def get_user(userid):
    result = User.list_user(sql_db,userid)
    return jsonify(result)

@app.route('/api/v1.0/user/add/<userid>/<name>/<email>/<phone>', methods=['GET','POST'])
def add_user(userid,name,email,phone):
     result = User.add_user(sql_db,userid,name,email,phone)
     return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False)
