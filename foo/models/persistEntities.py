import foo.models.entities as e
from foo import db

def create_participant(username, email, comment, eventId):
    cur = e.User(username=username, email=email, comment=comment, eventId=eventId)
    db.session.add(cur)
    db.session.commit()
    return "executed sucessfully"


def hello_again():
    return "hello again"

