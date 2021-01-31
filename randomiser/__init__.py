import os

from flask import Flask

from randomiser.config import Config


app = Flask(__name__)
app.config.from_object(Config)

from randomiser import routes