from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def sayHi():
    return "Hi"


@app.post("/")
def sayHitoUser(name=None, firstname=None):
    if name is None or firstname is None:
        return "key is None"
    elif name == "" or firstname == "":
        return "value is empty"
    else:
        return "Hi, " + name + " " + firstname
