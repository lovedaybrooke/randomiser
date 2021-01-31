import datetime

from randomiser import db


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    english = db.Column(db.String())
    german = db.Column(db.String())
    part_of_speech = db.Column(db.String())
    last_viewed = db.Column(db.DateTime, nullable=True)
