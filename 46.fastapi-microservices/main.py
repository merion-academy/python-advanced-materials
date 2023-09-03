from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from config import settings
from views import calc_router
from views import users_router
from views import permissions_router

app = FastAPI()
app.include_router(calc_router, prefix="/calc")
app.include_router(permissions_router, prefix="/permissions")
app.include_router(users_router, prefix="/users")
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors.allow_origins,
    allow_methods=settings.cors.allow_methods,
    allow_headers=settings.cors.allow_headers,
    allow_credentials=settings.cors.allow_credentials,
)


@app.get("/hello")
def hello_by_qs(name: str = "World"):
    return {"message": f"Hello {name}!"}


@app.get("/hello/{name}")
def hello_by_path(name: str):
    return {"message": f"Hello {name}!"}


@app.get("/hi")
@app.get("/hi/{name}")
def hi_by_path(name: str = "World"):
    return {"message": f"Hi {name}!!"}


if __name__ == "__main__":
    # print(settings.model_dump())
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
    )
