


from flask import Response
import json

def get_hello_world():
    resp = Response(response=json.dumps({'message': 'hello world GET!'}), status=200, mimetype='application/json')
    return resp

def post_hello_world():
    resp = Response(response=json.dumps({'message': 'hello world POST!'}), status=200, mimetype='application/json')
    return resp