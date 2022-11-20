from flask import Flask, request

app = Flask(__name__)


@app.get('/')
def hello_user():
    return 'Hello client'


@app.route('/',methods=['POST'])
def hello_to_username():
    data=request.args
    if not data.__contains__('name'):
        return 'Hello client'
    else:
        return 'Hello ' + data['name']


@app.route('/header', methods=['POST'])
def headers():
    data = request.headers
    if not data.__contains__('name'):
        return 'Hello user'
    else:
        return 'Hello  ' + data['name']


@app.route('/params', methods=['POST'])
def params():
    data = request.args
    if not data.__contains__('name'):
        return 'Hello user'
    else:
        return 'Hello  ' + data['name']


@app.route('/json', methods=['POST'])
def json():
    data = request.json
    if data is None or not data.__contains__('name'):
        return 'Hello user'
    else:
        return 'Hello ' + data['name']


if __name__ == '__main__':
    app.run(debug=True)
