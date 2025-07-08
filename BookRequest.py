from typing import Optional

from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID not needed for create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new Book",
                "author": "Albert Einstein",
                "description": "A new book description",
                "rating": 5
            }
        }
    }