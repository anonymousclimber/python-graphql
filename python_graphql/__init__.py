from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .constants import name, pw

app = Flask(__name__)
CORS(app)

# Databse Connections. 
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://"+name+":"+pw+"@localhost:5432/graphql"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



@app.route('/')
def hello():
    return 'Test'