from fastapi import APIRouter
from googleapiclient.discovery import build

from src.schemas.google_calendar import CalendarUpdate

router = APIRouter()


@router.post("/update_event", tags=["Google Calendar"])
def update_event(data: CalendarUpdate):
    service = build("calendar", "v3", credentials=data.get_credentials())
    event = (
        service.events()
        .patch(
            calendarId="primary",
            eventId=data.event_id,
            body={
                "summary": data.new_title,
                "start": {"dateTime": data.start},
                "end": {"dateTime": data.end},
            },
        )
        .execute()
    )
    return {"updated_event": event.get("id")}
