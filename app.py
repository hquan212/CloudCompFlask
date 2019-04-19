import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import logging

app = Flask(__name__)


MONGO_HOST = "mongodb://cluster0-shard-00-00-s1qny.mongodb.net"
MONGO_PORT = 27017
MONGO_DB = "BloodBank"
MONGO_USER = "sshjuser"
MONGO_PASS = "SSHJ678!"
client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client[MONGO_DB]
db.authenticate(MONGO_USER, MONGO_PASS)

# client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],27017)

db = client.tododb



@app.route('/')
def todo():

    _items = db.tododb.find()
    items = [item for item in _items]
    app.logging.info("Normal")
    return render_template('todo.html', items=items)


@app.route('/new', methods=['POST'])
def new():

    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    db.tododb.insert_one(item_doc)

    return redirect(url_for('todo'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
