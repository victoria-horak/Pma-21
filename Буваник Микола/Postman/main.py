from pydantic import BaseModel
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/")
def hello():
    return "Hello"


class Item(BaseModel):
    name: str


app = FastAPI()


@app.post("/body")
async def create_item(item: Item = None ):
    if item is None or item.name is None:
        return "Hello user"
    else:
        return "Hello " + item.name


@app.post("/header")
def read_items(name: str | None = Header(default=None, convert_underscores=False)):
    return "Hello " + name
@app.post("/request")
def read_items(name: str ):
    return "Hello " + name
