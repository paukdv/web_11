from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr


class ContactModel(BaseModel):
    id: int = 1
    first_name: str
    last_name: str
    phone_number: str
    birthday: date
    email: EmailStr
    additional_data: str


class ResponseContact(BaseModel):
    id: int = 1
    first_name: str
    last_name: str
    phone_number: str
    birthday: date
    email: EmailStr
    additional_data: Optional[str]

    class Config:
        or_mode = True
