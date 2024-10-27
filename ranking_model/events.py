from datetime import datetime, timezone

from fastapi import APIRouter, Request
from ics import Calendar
import requests


router = APIRouter()


@router.post("/get")
async def get_events(request: Request):
    data = await request.json()

    assert "calendar_url" in data

    calendar_url = data["calendar_url"]

    current_time = datetime.now(timezone.utc)
    day_end = datetime.now(timezone.utc).replace(hour=23, minute=59, second=59, microsecond=999)

    events = list()

    calendar = Calendar(requests.get(calendar_url).text)
    for e in calendar.events:
        event_begin = datetime.fromtimestamp(int(e.begin.timestamp()), tz=timezone.utc)
        event_end = datetime.fromtimestamp(int(e.end.timestamp()), tz=timezone.utc)

        if (event_end >= current_time) and (day_end >= event_begin):
            events.append({"name": e.name, "location": e.location, "begin": event_begin, "end": event_end})

    return {"events": events}
