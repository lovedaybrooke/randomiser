from flask import render_template

from randomiser import app
from randomiser.models import Card

@app.route('/')
def unfinished():
    return render_template('home.html', word_list = Card.pull())