from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/api")
async def read_root():
    return {"Hello": "api"}


@app.get("/{path}")
async def read_root(path: str):
    return {"Hello": "World", 'path': path}

