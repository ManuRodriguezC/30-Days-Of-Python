from fastapi import FastAPI, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Optional
from pydantic import BaseModel, Field
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

app = FastAPI()
app.title = "Mi aplicacion con fast API"
app.version = "0.0.2"

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth =  await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, datail="Credenciales invalidas")
        

class User(BaseModel):
    email: str
    password: str

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
                "id": "1",
                "title": "Scary Movie",
                "overview": "About the movie",
                "year": 2014,
                "rating": 7.8,
                "category": "Comedy"
            }
        }
    
    
    
movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora vieven los Navi",
        "year": "2009",
        "rating": 7.8,
        "category": "Accion"
    },
    {
        "id": 2,
        "title": "Avatar 2",
        "overview": "En un exuberante planeta llamado Pandora vieven los Navi",
        "year": "2022",
        "rating": 7.8,
        "category": "Romantica"
    }
]


@app.get("/", tags=['home'])
def massege():
    return HTMLResponse('<h1>Hello World!</h1>')


@app.post("/login", tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)


@app.get("/movies", tags=['movies'], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies():
    return JSONResponse(status_code=200,content=movies)


@app.get("/movies/{id}", tags=['movies'], status_code=200)
def get_movie(id: int = Path(ge=1, le=2000)):
    for movie in movies:
        if movie['id'] == id:
            return JSONResponse(status_code=200, content=movie)
    return JSONResponse(status_code=404,content=[])


@app.get("/movies/", tags=['movies'], status_code=200)
def get_movies_category(category: str = Query(min_length=4, max_length=20)):
    date = []
    for movie in movies:
        if movie["category"] == category:
            date.append(movie)
    return JSONResponse(status_code=200, content=date)

 
@app.post('/movies/', tags=['movies'], status_code=201)
def create_movie(movie: Movie):
    movies.append(movie)
    return JSONResponse(status_code=201, content={"message": "Successfull register"})


@app.put('/movies/{id}', tags=['movies'], status_code=205)
def put_movie( id: int, movie: Movie):
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
            return JSONResponse(status_code=205, content={"message": "Successfull update the movie"})
    return JSONResponse(content={"Not fount": "Movie"})


@app.delete('/movies/{id}', tags=['movies'])
def delet_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            return JSONResponse(status_code=200,
                                content={"message": "Successfull delete movie"})
    return JSONResponse(status_code=404,
                        content={"message": "Not found movie"})
        