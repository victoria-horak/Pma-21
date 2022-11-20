from flask import *

app = Flask(__name__)


@app.route("/hello")
def helloUser():
    return "Hello, User!"


@app.route("/hello", methods=['POST'])
def hello():
    username = request.args.get('username')
    if username is None or username is "":
        return "Hello, user"
    else:
        return "Hello, " + username + "!"


@app.route("/hello/Json", methods=['POST'])
def helloJson():
    request_data = request.get_json()
    if 'name' in request_data:
        return request_data['name']
    else:
        return "no name"

@app.route("/hello/Header", methods=['POST'])
def helloHeader():
    if request.headers.get('uname'):
        return request.headers.get('uname')
    else:
        return "no name"
