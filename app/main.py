from turtle import title
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import Settings
# postgres
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
settings = Settings()
# impot models
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# my_posts = [{"title": "fastapi", "content": "permier chapitre", "id": 1}, {
# "title": "fastapi mmm", "content": "permier chapitre", "id": 2}]


# def find_post(id):
# for p in my_posts:
#  if p["id"] == id:
# return p


# def find_index_post(id):
# for i, p in enumerate(my_posts):
# if p['id'] == id:
# return i


@app.get("/")
def root():
    return {"message": "Hello World asma::::"}


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
