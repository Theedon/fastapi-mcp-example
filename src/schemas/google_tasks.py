from pydantic import BaseModel


class TaskCreate(BaseModel):
    access_token: str
    task_title: str
    due: str | None = None

    def get_credentials(self):
        from google.oauth2.credentials import Credentials

        return Credentials(token=self.access_token)


class TaskDelete(BaseModel):
    access_token: str
    task_id: str

    def get_credentials(self):
        from google.oauth2.credentials import Credentials

        return Credentials(token=self.access_token)
