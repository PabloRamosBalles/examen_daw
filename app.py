from flask import Flask, jsonify
from objects import objects
from flask_mysqldb import MySQL
from flask_pymongo import PyMongo, MongoClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask('__name__')

app.config['MYSQL_USER'] = getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = getenv('MYSQL_DB')
app.config['MYSQL_HOST'] = getenv('MYSQL_HOST')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

db = MySQL(app)
mongo = PyMongo(app)

cli = mongo.MongoClient('localhost', 27017)

@app.route('/')
def index():
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM user')
    db.connection.commit()
    data = cur.fetchall()
    print(data)
    return jsonify({"objects": data, "message":"get all objects"})

@app.route('/<id>')
def getOne(id):
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM user where id = %s', (id,))
    db.connection.commit()
    data = cur.fetchone()
    print(data)
    if data:
        return ({"object": data})
    
@app.route('/add')
def add():
    cur = db.connection.cursor()
    cur.execute('INSERT INTO user values(null, "c", "c", 45)')
    db.connection.commit()
    data = cur.fetchone()
    print(data)
    if data:
         return 'object with added' 
    

@app.route('/delete/<id>')
def delete(id):
    cur = db.connection.cursor()
    cur.execute('DELETE FROM user where id = %s', (id,))
    db.connection.commit()
    data = cur.fetchone()
    print(data)
    if data:
        return 'object with id: '+id+' deleted' 
    
#----------------------------

@app.route('/mongo')
def mongo_index():
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM user')
    db.connection.commit()
    data = cur.fetchall()
    print(data)
    return jsonify({"objects": data, "message":"get all objects"})

@app.route('/mongo/<id>')
def mongo_getOne(id):
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM user where id = %s', (id,))
    db.connection.commit()
    data = cur.fetchone()
    print(data)
    if data:
        return ({"object": data})
    
@app.route('/mongo/add')
def mongo_add():
    cur = db.connection.cursor()
    cur.execute('INSERT INTO user values(null, "c", "c", 45)')
    db.connection.commit()
    data = cur.fetchone()
    print(data)
    if data:
        return ({"object": data})
    

@app.route('/mongo/delete/<id>')
def mongo_delete(id):
    cur = db.connection.cursor()
    cur.execute('DELETE FROM user where id = %s', (id,))
    db.connection.commit()
    data = cur.fetchone()
    print(data)
    if data:
        return ({"object": data})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')