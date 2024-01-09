#!/usr/bin/python3
""" View for states object """
from models.db_storage import to_dict
from flask import request, abort

@app.route(GET, "/api/v1/states")
@app.route(GET, "/api/v1/states/<state_id>")
if (<state_id> is None):
    abort(404)
@app.route(DELETE, "/api/v1/states/<state_id>"):
    return ({"": 200})
@app.route(POST, "/api/v1/status"):



