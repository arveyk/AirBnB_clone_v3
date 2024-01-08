#!/usr/bin/python3
""" Init file v1"""
from flask import Blueprint, Flask
from api.v1.views.index import *

app = Flask(__name__)
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

