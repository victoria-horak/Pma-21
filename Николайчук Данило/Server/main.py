from flask import *

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Hello, user.'

@app.route('/NameParams', methods=['POST'])
def helloUserNameParams():
    name = request.args.get("name")
    if name != "":
        return "Hello " + name + "."
    return "Hello no name."

@app.route('/NameJson', methods=['POST'])
def helloUserNameJson():
    requestData = request.get_json()
    name = requestData['username']
    if name != "":
        return "Hello " + name + "."
    return "Hello no name."

@app.route('/NameHeader', methods=['POST'])
def helloUserNameBody():
    name = request.headers.get("username")
    if name != "":
        return "Hello " + name + "."
    return "Hello no name."


app.run(port=8080)
