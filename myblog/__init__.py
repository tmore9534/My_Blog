from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SECRET_KEY']='19d895c43ecfd78685edefc3f860c65f'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'

db=SQLAlchemy(app)

from myblog import routes