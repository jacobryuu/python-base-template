from pydantic import BaseModel, Field


class AppSettings(BaseModel):
    app_name: str = Field(default="python-base-template")
    debug: bool = Field(default=False)
