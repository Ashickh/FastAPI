from pydantic import BaseModel
from typing import Optional


class Book(BaseModel):
    name: str
    price: float
    author: Optional[str] = None