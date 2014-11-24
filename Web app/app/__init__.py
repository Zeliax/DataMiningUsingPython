from flask import Flask

app = Flask(__name__)  # defining the app
app.config.from_object('app.config')

from app import views
