from fastapi import FastAPI, HTTPException
from schema import url_choices, BandBase, BandwithId, BandCreate

app= FastAPI()

BANDS = [
    {"id": 0, "name": "The Beatles", "genre": "Rock"},
    {"id": 1, "name": "The Beatles", "genre": "Rock"},
    {"id": 2, "name": "Nirvana", "genre": "Grunge"},
    {"id": 3, "name": "Black sem", "genre": "Metal",'albums': [{'title': 'Black Album', 'release_year': '1991-08-12'}]},
    {"id": 4, "name": "The Rolling Stones", "genre": "Electronic"},
]

@app.get("/bands")
async def bands(
    genre: url_choices | None= None,
    has_albums: bool =False
    ) -> list[BandwithId]:
    band_list = [BandwithId(**b) for b in BANDS]                #  Convert each band dictionary to a Band model instance, PREVIOUSLY WE WERE CONVETING TO PYDANTIC MODEL ON RETURN 
    if genre:
        band_list= [b for b in band_list if b.genre.lower() == genre.value]
    if has_albums:
        band_list = [b for b in band_list if len(b.albums)>0]
    return band_list


@app.get("/bands/{band_id}", status_code=206)
async def band(band_id: int) -> BandwithId:
    for band in BANDS:
        if band["id"] == band_id:
            return BandwithId(**band)
       
    raise HTTPException(status_code=404, detail="Band not found")        


@app.get("/bands/genre/{genre}")
async def bands_by_genre(genre: url_choices) -> list[dict]:
    # filtered_bands = [band for band in BANDS if band["genre"].lower() == genre.lower()]  # basic
    filtered_bands = [band for band in BANDS if band["genre"].lower() == genre.value]  # using enum funcitonality
    if not filtered_bands:
        raise HTTPException(status_code=404, detail="No bands found for this genre")
    return filtered_bands


@app.post("/bands" , status_code=201)
async def create_band(band_data: BandCreate) -> BandwithId:
    id=BANDS[-1]["id"] + 1 if BANDS else 1
    band= BandwithId(id=id, **band_data.model_dump()).model_dump()  # Convert BandCreate to BandwithId
    BANDS.append(band)
    return band