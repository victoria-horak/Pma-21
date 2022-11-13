from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello_user():
    return 'Hello user'


@app.post('/')
def hello_to_username(name):
    if name is None:
        return 'There is no username'
    else:
        return 'Hello ' + name
