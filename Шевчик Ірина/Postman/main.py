from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return 'Hello, user'


@app.route('/', methods=['POST'])
def index():
    if request.method == "POST":
        data = request.form
        if not data['first_name'] is None:
            return "Incorrect data"
        else:
            return 'Hello  ' + data['first_name']


if __name__ == '__main__':
    app.run(debug=True)
