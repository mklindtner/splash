import foo.models.entities as e
from foo import db

def create_participant(username, email, comment, eventId):
    cur = e.User(username=username, email=email, comment=comment, eventId=eventId)
    #Yes this is trash, Yes this is a hackathon, Yes you need to be smart about the evaluation if the db grows
    #also use try/except 
    allUsers = e.User.query.all()

    for user in allUsers:        
        if user.email == cur.email or user.username == cur.username:
            return "email or username already exists" 
        
    db.session.add(cur)    
    db.session.commit()
    return "executed sucessfully"


def get_participants(eventId):
    participants = e.User.query.filter(e.User.eventId == eventId).all()
    return participants


def hello_again():
    return "hello again"

