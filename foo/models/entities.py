from foo import db

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    comment = db.Column(db.String(120), unique=False)
    eventId = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# def commitToDb(model):
#     db.session.add(model)
#     db.session.commit()


# def reset_db():
#     db.drop_all()
#     db.create_all()