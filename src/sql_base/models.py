from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Workers(BaseModel):
    post_id: Optional[int]
    surname: str
    name: str
    middle_name: str
    phone_number: str

class Hall(BaseModel):
    hall_id: Optional[int]
    title_hall: str
    floor: int

class Excursion(BaseModel):
    excursion_id: Optional[int]
    floor: int
    exhibition_id: Optional[int]
    workers_id: Optional[int]
    info_id: Optional[int]

class Exhibition_exhibits(BaseModel):
    exhibit_id: Optional[int]
    hall_id: Optional[int]
    title_exhibits: str
    date_of_discovery: Optional[datetime]

class Information_about_the_excursion(BaseModel):
    info_id: Optional[int]
    user_id: Optional[int]
    workers_id: Optional[int]
    number_of_people: int

class Post(BaseModel):
    post_id: Optional[int]
    post: str

class User(BaseModel):
    user_id: Optional[int]
    user_name: str
    user_password: str