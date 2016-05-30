from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app import app 


app.config.from_object('config')
db = SQLAlchemy(app)