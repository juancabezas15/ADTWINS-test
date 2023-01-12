from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    id: Optional[str] = None
    name: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
