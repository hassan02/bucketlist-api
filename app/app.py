from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask.ext.api import FlaskAPI
from flask.ext.api.exceptions import \
    AuthenticationFailed, NotFound, NotAcceptable, ParseError
from .decorators import auth
from flask_restful import Api

from helpers import messages
from resources import *


app = Flask(__name__)
app.config.from_object('config')
app.config["JSON_SORT_KEYS"] = False

api = Api(app)
api.add_resource(LoginUser, "/auth/login")
api.add_resource(RegisterUser, "/auth/register")
api.add_resource(AllBucketLists, "/api/v1/bucketlists/")
api.add_resource(SingleBucketList, "/api/v1/bucketlists/<int:id>")
api.add_resource(AllBucketListItems, '/api/v1/bucketlists/<int:id>/items/')
api.add_resource(SingleBucketListItem, '/api/v1/bucketlists/<int:id>/items/<int:item_id>')

@app.route("/", methods = ["GET","POST"])
def home_page(): 
    return 'Hello World! Welcome to BucketList Manager. Please login/register to access our services'

@app.errorhandler(404)
def handle_error(message):
    return messages["resource_not_found"], 404