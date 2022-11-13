
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hom_page():
    return "Hello"


@app.post("/")
def hello_first_name(hello_first_name=None):
    if hello_first_name is None:
        return "Not give user"
    else:
        return "Hello " + hello_first_name
