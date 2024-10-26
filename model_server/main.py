import os

import uvicorn
from fastapi import FastAPI

from events import router as event_router
from locations import router as location_router


app = FastAPI()


app.include_router(event_router, prefix="/events")
app.include_router(location_router, prefix="/locations")


@app.get("/")
def index() -> None:
    return {"msg": "Hello, World!"}


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

    uvicorn.run(app, host=os.getenv("APP_HOST"), port=int(os.getenv("APP_PORT")))
