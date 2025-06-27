from pydantic import BaseModel


class CalendarUpdate(BaseModel):
    access_token: str
    event_id: str
    new_title: str
    start: str
    end: str

    def get_credentials(self):
        from google.oauth2.credentials import Credentials

        return Credentials(token=self.access_token)
