from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

import foo.models.persistEntities as pe
# import models.db.persistEntities as pe

@app.route('/')
def hello_world():
    return render_template("index.html", title="Home")

@app.route('/signup')
def signup():
    return render_template("signup.html", title="Signup")


@app.route('/signup/applicant', methods=['POST'])
def create_applicant():
    name = request.form['user1']
    comment = request.form['password1']
    email_address = request.form['email']
    eventId = request.form['eventId1']
    return pe.create_participant(name, comment, email_address, eventId)
    # return '{} : {} : {} : {}'.format(name, comment, email_address, eventId)


# if __name__ == '__main__':
#     app.run()


