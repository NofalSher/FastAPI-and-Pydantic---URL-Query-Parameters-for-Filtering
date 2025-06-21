from enum import Enum
from pydantic import BaseModel,field_validator
from datetime import date

class url_choices(Enum):
    Rock = "rock"
    Grunge = "grunge" 
    Electronic = "electronic"
    Metal = "metal"
    Pop = "pop"
    HipHop = "hiphop"
    
class genre_choices(Enum):
    Rock = "Rock"
    Grunge = "Grunge"
    Electronic = "Electronic"
    Metal = "Metal"
    Pop = "Pop"
    HipHop = "HipHop"


class Album(BaseModel):
    title: str
    release_year: date
    
class BandBase(BaseModel):
    name: str
    genre:genre_choices
    albums: list['Album']=[]

    # A band can have album , but some may not have any albums so default is empty list
class BandCreate(BandBase):
    @field_validator('genre', mode='before')
    def titlecase_name(cls, v):
        return v.title()

class BandwithId(BandBase):
    id: int