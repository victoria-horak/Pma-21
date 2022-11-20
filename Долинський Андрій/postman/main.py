from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def greeting():
    return "Hello"


@app.post("/")
def greetingUser(name=None):
    if name == None:
        return "No given user"
    else:
        return "Hello, " + name