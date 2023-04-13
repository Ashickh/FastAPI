from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

sample_db = {}



@app.get("/")
def get_item():
    return "This Is A Test"

@app.get("/get_books/{book_id}")
def get_item(book_id: int):
    return sample_db[book_id]

@app.post("/create_books/{book_id}")
def create_book(book_id: int, book: Book):
    if book_id in sample_db:
        return {"error":"Book Already Exists"}
    sample_db[book_id] = book
    return sample_db[book_id]

# @app.post("/create_items/{item_id}")
# def create_item(item_id: int, item: Item):
#     if item_id in inventory:
#         return {"Error":"Item ID already exists"}
#     inventory[item_id] = item
#     return inventory[item_id]
