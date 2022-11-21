from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def default_route():
    if request.method == 'GET':
        return "Hello user"
    elif request.method == "POST":
        data = request.form
        if not data.__contains__('first_name'):
            return 'Hello user'
        else:
            return 'Hello  ' + data['first_name']


@app.route('/header', methods=['GET', 'POST'])
def headers():
    if request.method == 'GET':
        return 'Hello user'
    elif request.method == "POST":
        data = request.headers
        if not data.__contains__('first_name'):
            return 'Hello user from header'
        else:
            return 'Hello  ' + data['first_name']


@app.route('/params', methods=['GET', 'POST'])
def params():
    if request.method == 'GET':
        return 'Hello user'
    elif request.method == "POST":
        data = request.args
        if not data.__contains__('first_name'):
            return 'Hello user'
        else:
            return 'Hello  ' + data['first_name']


@app.route('/json', methods=['GET', 'POST'])
def json():
    if request.method == 'GET':
        return 'Hello user'
    elif request.method == "POST":
        data = request.json
        if data is None or not data.__contains__('first_name'):
            return 'Hello user from json'
        else:
            return 'Hello ' + data['first_name']


if __name__ == '__main__':
    app.run(debug=True)
