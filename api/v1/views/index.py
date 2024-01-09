#!/usr/bin/python3
""" Index blueprint? """
from api.v1.views import app_views
from flask import Flask

@app_view.route("/status"):
    """ Creating a status route """
    def status():
        """ returns the json desc below """
        json = {"status" : "OK"}
        return json
