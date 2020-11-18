from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager
import os

app = Flask(__name__)
app.secret_key = "^%@&^@*&!@67532623^@%^%@!"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/saledbv1?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['ROOT_PROJECT_PATH'] = os.path.join(app.root_path, '/saleappv11/saleapp')

db = SQLAlchemy(app=app)
admin = Admin(app=app, name="IT81 SHOP", template_mode="bootstrap4")
login = LoginManager(app=app)