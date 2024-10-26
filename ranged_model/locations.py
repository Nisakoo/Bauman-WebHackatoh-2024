from fastapi import APIRouter


router = APIRouter()


@router.get("/get")
def get_locations(location: str):
    return {"locations": [location]}
