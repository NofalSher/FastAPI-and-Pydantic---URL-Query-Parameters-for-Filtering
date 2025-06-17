from enum import Enum
from pydantic import BaseModel
from datetime import date

class url_choices(Enum):
    Rock = "rock"
    Grunge = "grunge" 
    Electronic = "electronic"
    Metal = "metal"
    Pop = "pop"
    HipHop = "hiphop"
    

class Album(BaseModel):
    title: str
    release_year: date
    
class Band(BaseModel):
    id: int
    name: str
    genre:str
    albums: list['Album']=[]        # A band can have album , but some may not have any albums so default is empty list
