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
