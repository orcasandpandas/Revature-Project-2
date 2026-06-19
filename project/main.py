import httpx
import logging
from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.security import APIKeyHeader
from starlette import status
from typing import Optional
from fastapi.responses import JSONResponse as _JSONResponse
# Import our models
from models import Movie, MovieResponse
from routers import router as movie_router
from auth import router as auth_router

# API Key: 034f84e71360ce56922495f811ae84d6

# API Read access token: eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMzRmODRlNzEzNjBjZTU2OTIyNDk1ZjgxMWFlODRkNiIsIm5iZiI6MTc4MTgxNTY2MC4xNDgsInN1YiI6IjZhMzQ1OTZjYTQ5NzZiYjYyOGQwYWFmYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Gr9QI7VAy2F8PN5gXZE8aiEjrVWg8jh5C_jfhXQYzpw

TMDB_API_KEY = "034f84e71360ce56922495f811ae84d6"
TMDB_BASE_URL = "https://api.themoviedb.org/3"





app = FastAPI(
    title="Movies API",
    description="A simple API for managing movies.",
    version="1.0.0"
)

app.include_router(movie_router)
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movies API!"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)