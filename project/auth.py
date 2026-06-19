import secrets
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette import status

app = FastAPI(title="Movies API",version="1.0.0")

security = HTTPBasic()

USERS = {
    "admin": "password123",
    "user1": "mypassword"
}

def get_user(credentials: HTTPBasicCredentials = Depends(security)) -> str:
    stored_password = USERS.get(credentials.username, "")
    password_correct = secrets.compare_digest(
        credentials.password.encode('utf-8'), 
        stored_password.encode('utf-8')
    )
    if not password_correct:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/movies/me", tags=["Auth"])
def get_my_profile(username: str = Depends(get_user)):
    return {
        "username": username,
        "message": f"Hello {username}, you are authenticated."
    }

@app.get("/movies", tags=["Auth"])
def get_employees(username: str = Depends(get_user)):
    return {"Users": [], "requested_by": username}

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Movies API"}       