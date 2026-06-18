import logging
from fastapi import FastAPI, Depends
from fastapi.requests import Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.security import APIKeyHeader
from starlette import status
from typing import Optional
from fastapi.responses import JSONResponse as _JSONResponse
# Import our models
from models import MovieResponse

# API Key: 034f84e71360ce56922495f811ae84d6

# API Read access token: eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMzRmODRlNzEzNjBjZTU2OTIyNDk1ZjgxMWFlODRkNiIsIm5iZiI6MTc4MTgxNTY2MC4xNDgsInN1YiI6IjZhMzQ1OTZjYTQ5NzZiYjYyOGQwYWFmYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Gr9QI7VAy2F8PN5gXZE8aiEjrVWg8jh5C_jfhXQYzpw

app = FastAPI(
    title="Movies API",
    description="A simple API for managing movies.",
    version="1.0.0"
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)