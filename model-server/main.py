from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def index() -> None:
    return {"msg": "Hello, World!"}
