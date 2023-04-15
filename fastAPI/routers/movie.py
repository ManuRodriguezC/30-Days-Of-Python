from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import  JSONResponse
from config.database import session
from models.movies import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middelewares.jwt_bearer import JWTBearer
from service.movie import MovieService
from schemas.movie import Movie


movie_router = APIRouter()



@movie_router.get("/movies", tags=['movies'], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies():
    db = session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.get("/movies/{id}", tags=['movies'], status_code=200)
def get_movie(id: int = Path(ge=1, le=2000)):
    db = session()
    result = MovieService(db).get_movie(id)
    if result:
            return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={"message": "Not found movie with this id"})


@movie_router.get("/movies/", tags=['movies'], status_code=200)
def get_movies_category(category: str = Query(min_length=4, max_length=20)):
    db = session()
    result = MovieService(db).get_category(category)
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=200, content={"message": "Not found the movie with this category"})

 
@movie_router.post('/movies/', tags=['movies'], status_code=201)
def create_movie(movie: Movie):
    db = session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Successfull register"})


@movie_router.put('/movies/{id}', tags=['movies'], status_code=205)
def put_movie( id: int, movie: Movie):
    db = session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not found the movie with this id"})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=200, content={"message": "Successfull update the movie"})


@movie_router.delete('/movies/{id}', tags=['movies'])
def delet_movie(id: int):
    db = session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not found movie"})
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Successfull delete movie"})
