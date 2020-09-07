# import db_connectivity
import os
from flask import Flask, render_template, request
import json
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(os.environ["DB_PORT_27017_TCP_ADDR"], 27017)

db = client.test
# postgres_client = db_connectivity.postgres_connect()
# print(postgres_client)
# cursor_connection = postgres_client.cursor()


@app.route('/insert', methods = ['POST'])
def insert():
    try:
        user_collection = db.users
        if request.method == 'POST':
            Name = request.form['name']
            Age = request.form['age']
            print("--name--", Name)
            data = user_collection.insert_one({"Name": Name, "age": Age})
            # insert_query = ("""INSERT INTO users (Name, Age) VALUES (%s, %s);""")
            # record = (Name, Age)
            # data = cursor_connection.execute(insert_query, record)
            # postgres_client.commit()
            return render_template('user.html', Name= data)

    except Exception:

        return '<h2> Insertion Failed <h2>'


@app.route('/insert')
def index_show():
     return render_template('user.html')


@app.route('/find', methods = ['GET'])
def find():
    user_collection = db.users
    if request.method == 'GET':
        users = user_collection.find()
        print("-----users---", users)

        return render_template('user_list.html', name=users)

@app.route('/update_record', methods = ['POST'])
def update():
    user_collection = db.users
    if request.method == 'POST':
        myquery = { "Name": request.form['name'] }
        newvalues = { "$set": { "age": request.form['age']} }
        print(myquery)
        print(newvalues)
        data = user_collection.update_one(myquery, newvalues)
        print(data)
        # Name = request.form['name']
        # Age = request.form['age']
        # update_query = ("""UPDATE users SET age = %s where name = %s;""")
        # record = (Age, Name)
        # data = cursor_connection.execute(update_query, record)
        # postgres_client.commit()
        return render_template('update.html', Name= data)

    # return '<h1> Updated the record successfully </h1>'

@app.route('/update_record')
def index_shower():
    return render_template('update.html')


@app.route('/delete_record', methods = ['POST'])
def delete():
    user_collection = db.users

    if request.method == 'POST':

        users = user_collection.delete_one(
        {
            "Name":request.form['name']
        })

        # Name = request.form['name']
        # print(Name)
        # query = """DELETE from users Where name = %s;"""
        # users = cursor_connection.execute(query, (Name, ))
        # postgres_client.commit()

        return render_template('delete.html', Name= users)

    # return '<h1> Deleted the record successfully </h1>'

@app.route('/delete_record')
def index_showes():
    return render_template('delete.html')


# @app.route('/display')
# def read():
#     try:
#         cursor_connection.execute("""SELECT * from users""")
#         rows = cursor_connection.fetchall()
#         return render_template('index.html', name = rows)

#     except Exception as e:
#         print(e)
#         return {}

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
