from api.app import app
from flask import request, make_response, jsonify
from helpers.mongoConnection import get_name, insert_data
from bson import json_util
import os
from flask_pymongo import PyMongo

app.config['MONGO_DBNAME'] = 'apichat'
app.config["MONGO_URI"] = "mongodb://localhost:27017/apichat"
mongo = PyMongo(app)

@app.route("/insert/<collection>")
def insert(collection):
    return json_util.dumps(insert_data(collection, dict(request.args)))

@app.route("/find/<name>")
def find(name):
    user = mongo.db.users.find_one_or_404({"name":name})
    return f'''
        <h1>{name}</h1>
    '''

@app.route('/fetch', methods=['GET'])
def get_all_names():
  name = mongo.db.users
  output = []
  for user in users.find():
    output.append({'name' : user['name']})
  return jsonify({'result' : output})


@app.route("/update/<collection>/<filt>/<data>")
def update(collection,filt,data):
    return json_util.dumps(update_data(collection, dict(request.args), dict(request.args)))




#@app.route("/api/v1/users/", methods=['GET', 'POST', 'PUT'])
#def users():

@app.route("/")
def hello():
    headers = {"Content-Type": "application/json"}
    return make_response('it worked!', 200, headers)

@app.route("/g", methods=['GET'])
def g():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    headers = {"Content-Type": "application/json"}
    return make_response('it worked!', 200, headers)

@app.route('/postname', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    user = User.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.update(email=record['email'])
    return jsonify(user.to_json())

