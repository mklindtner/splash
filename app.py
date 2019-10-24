# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from foo import app

if __name__ == '__main__':
    app.run()

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
