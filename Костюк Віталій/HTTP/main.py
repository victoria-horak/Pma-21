
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def default_value():
    return "Hello"


@app.post("/")
def first_name(first_name):
    if first_name is None:
        return "Not given username"
    else:
        return "Hello " + first_name
