import datetime

from sqlalchemy import func

from randomiser import db


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    english = db.Column(db.String())
    german = db.Column(db.String())
    part_of_speech = db.Column(db.String())
    last_viewed = db.Column(db.DateTime, nullable=True)

    @classmethod
    def pull(cls):
        unseen_cards = Card.query.filter_by(last_viewed=None)
        verb = unseen_cards.filter_by(part_of_speech="verb").order_by(
               func.random()).first()
        noun = unseen_cards.filter_by(part_of_speech="noun").order_by(
               func.random()).first()
        adj = unseen_cards.filter_by(part_of_speech="adjective/adverb"
              ).order_by(func.random()).first()
        extra = unseen_cards.filter(Card.part_of_speech != 'verb').order_by(
                func.random()).first()
        word_list = [verb, noun, adj, extra]
        cls.update_dates(word_list)
        return word_list

    @classmethod
    def update_dates(cls, items):
        for item in items:
            item.last_viewed = datetime.datetime.today()
            db.session.add(item)
        db.session.commit()

