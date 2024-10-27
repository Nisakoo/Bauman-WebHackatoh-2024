from datetime import datetime, timezone

from fastapi import APIRouter
from ics import Calendar
import requests


router = APIRouter()


@router.get("/get")
def get_events(calendar_url: str):
    current_time = datetime.now(timezone.utc)
    day_end = datetime.now(timezone.utc).replace(hour=23, minute=59, second=59, microsecond=999)

    events = list()

    calendar = Calendar(requests.get(calendar_url).text)
    for e in calendar.events:
        event_begin = datetime.utcfromtimestamp(int(e.begin.timestamp())).replace(tzinfo=timezone.utc)
        event_end = datetime.utcfromtimestamp(int(e.end.timestamp())).replace(tzinfo=timezone.utc)

        if (event_end >= current_time) and (day_end >= event_begin):
            events.append({"name": e.name, "location": e.location, "begin": event_begin, "end": event_end})

    return events
