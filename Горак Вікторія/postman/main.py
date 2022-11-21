from flask import Flask, request

app = Flask(__name__)


@app.get('/')
def hello_user():
    return 'Hello client'


@app.route('/', methods=['POST'])
def hello_to_username():
    client_host = request.args
    if client_host.__contains__('name'):
        return 'Hello ' + client_host['name']
    else:
        return 'Hello client'


@app.route('/header', methods=['POST'])
def headers_func():
    client_host = request.headers
    if client_host.__contains__('name'):
        return 'Hello  ' + client_host['name']
    else:
        return 'Hello client'


@app.route('/params', methods=['POST'])
def params_func():
    client_host = request.args
    if client_host.__contains__('name'):
        return 'Hello  ' + client_host['name']
    else:
        return 'Hello client'


@app.route('/json', methods=['POST'])
def json_func():
    client_host = request.json
    if client_host.__contains__('name'):
        return 'Hello ' + client_host['name']
    else:
        return 'Hello client'


if __name__ == '__main__':
    app.run(debug=True)
