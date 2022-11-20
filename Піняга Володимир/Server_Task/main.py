from flask import *

app = Flask(__name__)


@app.route('/')
def getName():
    return "Hello, user."


@app.route('/Name', methods=['POST'])
def helloUserName(name):
    if name is not None:
        return "Hello" + name
    return "Hello noname"


if __name__ == '__main__':
    app.run(port=5000)
