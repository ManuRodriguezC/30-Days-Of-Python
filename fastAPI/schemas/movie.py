from pydantic import BaseModel, Field
from typing import Optional


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=15)
    overview: str = Field(max_length=100)
    year: int = Field(le=2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(max_length=30, min_length=5)
    
    class Config():
        schema_extra = {
            "example": {
                "title": "Scary Movie",
                "overview": "About the movie",
                "year": 2014,
                "rating": 7.8,
                "category": "Comedy"
            }
        }
