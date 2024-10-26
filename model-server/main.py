from fastapi import FastAPI

from .events import router as event_router


app = FastAPI()


app.include_router(event_router, prefix="/events")


@app.get("/")
def index() -> None:
    return {"msg": "Hello, World!"}
