#!/usr/bin/python3
""" App module """
from api_views import app.vi.views
from flask import Blueprint, Flask, render_template
from models import storage

app = Flask(__name__)
app_views = Blueprint('app_views', __name__)


@app.teardown_appcontext():
    """ Function to call storage.close() """
    storage.close()


if __name__ == '__main__':
    """ prevents execution when this module is imported"""
    if (!HBNB_API_HOST or !HBNB_API_PORT):
        app.run(host=0.0.0.0, port=5000, threaded=True)
    elif (!HBNB_API_HOST):
        app.run(host=0.0.0.0, HBNB_API_PORT, threaded=True)
    elif (!HBNB_API_PORT):
        app.run(HBNB_API_HOST, port= 5000, threaded=True)
