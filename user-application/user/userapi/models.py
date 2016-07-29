import os
import sys
import sqlite3
import json
import argparse

""" Program to check the version of Python and Exit """
def pversion():
   "Checking Python Version required to run this program"
   if sys.version_info < (3, 4):
       return ("This program requires Python 3.4+..exiting")
       sys.exit(99)

""" Check if the database in the directory exists, if not initialize it """
def init_db(db_name):
    print ("Initializing new database %s" % db_name )

    # Connecting to the database file
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Drop any tables
    c.execute("""drop table if exists users""")
    conn.commit ()

    # Create tables with schema
    c.execute("""create table users (
    id INTEGER PRIMARY KEY,
    userid TEXT UNIQUE not NULL,
    username TEXT,
    email TEXT,
    phone INTEGER)""")

    c.execute("""insert into users values (NULL,"admin","Admin User","admintest@gmail.com",6362455555)""")

    conn.commit()
    conn.close()

""" Function to list users """
def list_users (db_name):
      try:

        def dict_factory(cursor, row):
            d = {}
            for idx, col in enumerate(cursor.description):
               d[col[0]] = row[idx]
            return d

        connection = sqlite3.connect(db_name)
        connection.row_factory = dict_factory

        cursor = connection.cursor()
        # cursor.execute("select userid,username,email,phone from users")
        cursor.execute("select userid from users")

        results = cursor.fetchall()
        return (results)
        # print (json.dumps(results,indent=2))


      except sqlite3.Error:
        print ("Error %s:" % args[0])
        sys.exit(1)

      finally:
        if connection:
           connection.close()

def list_user (db_name,user_name):
      try:

        def dict_factory(cursor, row):
            d = {}
            for idx, col in enumerate(cursor.description):
               d[col[0]] = row[idx]
            return d

        connection = sqlite3.connect(db_name)
        connection.row_factory = dict_factory

        cursor = connection.cursor()
        # cursor.execute("select userid,username,email,phone from users")

        # cursor.execute("select * from users where userid=?", (user_name))
        # textvar = '%{}%'.format(UserID)
        # cursor.execute("select * from users where userid like ?", (textvar,))

        textvar = '{}'.format(user_name)
        cursor.execute("select userid,username,email,phone from users where userid=?", (textvar,))

        results = cursor.fetchall()

        # print (json.dumps(results,indent=2))
        return (results) 

      except sqlite3.Error:
        print ("Error %s:" % args[0])
        sys.exit(1)

      finally:
        if connection:
           connection.close()

def delete_user (db_name,user_name):
      try:

        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        textvar = '{}'.format(user_name)
        c.execute('DELETE FROM users WHERE userid=?', (textvar,))

        conn.commit()
        print ("200: record deleted")

      except sqlite3.Error:
        print ("Error %s:" % args[0])
        sys.exit(1)

      finally:
        if conn:
           conn.close()

def update_user (db_name,user_name):
      try:

        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        textvar = '{}'.format(user_name)
        c.execute('select username,email,phone FROM users WHERE userid=?', (textvar,))
        record=c.fetchone()

        user_Name=(record[0])
        eMail=(record[1])
        pHone=(record[2])

        print("Current User name: ",user_Name)
        n_user_Name = input("update user name :")
        if not n_user_Name:
           n_user_Name=user_Name

        print("Current Email: ",eMail)
        n_eMail = input("update email: ")
        if not n_eMail:
           n_eMail=eMail

        print("Current Phone Number: ",pHone)
        n_pHone = input("update pHone: ")
        if not n_pHone:
           n_pHone=pHone

        # print(n_user_Name,n_eMail,n_pHone)
        # sql1=('UPDATE users SET username=?, email=?, phone=? WHERE userid=?', (n_user_Name,n_eMail,n_pHone,textvar,))
        # c.execute('UPDATE users SET username=n_user_Name,email=n_eMail,phone=n_pHone WHERE userid=?', (textvar,))
        c.execute('UPDATE users SET username=?, email=?, phone=? WHERE userid=?', (n_user_Name,n_eMail,n_pHone,textvar,))
        conn.commit()

      except sqlite3.Error:
        print ("Error %s:" % args[0])
        sys.exit(1)

      finally:
        if conn:
           conn.close()



# def add_user (db_name):
# We now check if the id,name,email and phone number as passed along from API and accept them without prompts

def add_user (db_name,userID,userName,userEmail,userPhone):

    try:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute('INSERT INTO users VALUES (NULL, ?, ?, ?, ?)',(userID,userName,userEmail,userPhone))
        conn.commit()

    # except sqlite3.Error:
    except Exception as err:
        return(err)

    finally:
        if conn:
            conn.close()
