from fastapi import FastAPI
from config.database import engine, Base
from middelewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.login import login_router

app = FastAPI()
app.title = "Mi aplicacion con fast API"
app.version = "0.0.2"

app.add_middleware(ErrorHandler)
app.include_router(login_router)
app.include_router(movie_router)

Base.metadata.create_all(bind=engine)     
