#!/usr/bin/python3
""" Index Module for views"""
from api.v1.views import app_views
from flask import Flask


if __name__ == '__main__':
    @app_views.route():
        """ rounte for views """
        json =  {"status": "ok" }
        return json

