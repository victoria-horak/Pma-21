from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    return 'Hello, user'

@app.route('/', methods=['POST'])
def say_hello_to_username():
    body = request.form
    response = 'Hello, '
    if not body.__contains__('username'):
        response = response + 'default user'
    else:
        response = response + body['username'];
    return response


app.run(port=8080)