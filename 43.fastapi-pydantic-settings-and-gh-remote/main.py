from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from config import settings
from views.calc import router as router_calc

app = FastAPI()
app.include_router(router_calc, prefix="/calc")
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
