from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse
from jwt_manager import create_token

login_router = APIRouter()

class User(BaseModel):
    email: str
    password: str

@login_router.get("/", tags=['home'])
def massege():
    return HTMLResponse('<h1>Hello World!</h1>')


@login_router.post("/login", tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)
  