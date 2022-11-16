from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return 'Hello, user'

    elif request.method == 'POST':
        name = request.form
        if not name.__contains__('first_name'):
            return "There is no name"
        else:
            return "Hello " + name['first_name']


if __name__ == '__main__':
    app.run(debug=True)
