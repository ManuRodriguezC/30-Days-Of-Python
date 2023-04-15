from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import Optional
from pydantic import BaseModel, Field
from config.database import session
from models.movies import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middelewares.jwt_bearer import JWTBearer


movie_router = APIRouter()

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


@movie_router.get("/movies", tags=['movies'], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies():
    db = session()
    result = db.query(MovieModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.get("/movies/{id}", tags=['movies'], status_code=200)
def get_movie(id: int = Path(ge=1, le=2000)):
    db = session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if result:
            return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={"message": "Not found movie with this id"})


@movie_router.get("/movies/", tags=['movies'], status_code=200)
def get_movies_category(category: str = Query(min_length=4, max_length=20)):
    db = session()
    result = db.query(MovieModel).filter(MovieModel.category == category).all()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=200, content={"message": "Not found the movie with this category"})

 
@movie_router.post('/movies/', tags=['movies'], status_code=201)
def create_movie(movie: Movie):
    db = session()
    new_movie = MovieModel(**movie.dict())
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Successfull register"})


@movie_router.put('/movies/{id}', tags=['movies'], status_code=205)
def put_movie( id: int, movie: Movie):
    db = session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if result:
        result.title = movie.title
        result.overview = movie.overview
        result.year = movie.year
        result.rating = movie.rating
        result.category = movie.category
        db.commit()
        return JSONResponse(status_code=205, content={"message": "Successfull update the movie"})
    return JSONResponse(status_code=200, content={"message": "Not found the movie with this category"})

@movie_router.delete('/movies/{id}', tags=['movies'])
def delet_movie(id: int):
    db = session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if result:
        db.delete(result)
        db.commit()
        return JSONResponse(status_code=200, content={"message": "Successfull delete movie"})
    return JSONResponse(status_code=404, content={"message": "Not found movie"})
