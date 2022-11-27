from datetime import datetime
from flask import *
from server import app

@app.route('/hello', methods=['GET'])
def initial_page():
    return 'Hello, user'

@app.route('/hellouser', methods=['POST'])
def say_hello():
    body = request.args
    response = 'Hello, '
    if not body.__contains__('username'):
        response = response + 'user'
    else:
        response = response + body['username']
    return response