from flask import Flask, render_template, json, request, redirect, session
from flask import Markup
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from flask import session

mysql = MySQL()
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.secret_key = 'My secret key?'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'T!nley00'
app.config['MYSQL_DATABASE_DB'] = 'obesityDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

