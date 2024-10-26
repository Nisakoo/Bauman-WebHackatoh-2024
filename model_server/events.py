from datetime import datetime

from fastapi import APIRouter


router = APIRouter()


@router.get("/get")
def get_events(calendar_url: str, start_datetime: datetime, end_datetime: datetime):
    # Getting calendart...
    # Create empty list
    # Get events end_datetime >= BEGIN >= start_datetime
    # Each event: Dict with NAME, LOCATION, BEGIN, END
    events = list()

    return events
