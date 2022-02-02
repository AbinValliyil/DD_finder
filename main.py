from geopy.geocoders import Nominatim
from geopy import distance
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from schemas import AZA_geocode


app=FastAPI( title="AZA [Distance_Finder]" ,

  contact={
        "name": "Abin_michael",

        "email": "abinvalliyil@gmail.com"
             
                          })



origins = [
    "http://localhost:3000",
    "https://azza.vercel.app"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post('/distance_finder')
def d_finder(code:AZA_geocode):
  geocoder =Nominatim(user_agent='python')
  location1=code.pin1
  location2=code.pin2
  cor1 =geocoder.geocode(location1)
  cor2 =geocoder.geocode(location2)
  lat1,log1 =(cor1.latitude),(cor1.longitude)
  lat2,log2 =(cor2.latitude),(cor2.longitude)
  place1=(lat1,log1)
  place2=(lat2,log2)
  
  
    
  return {"distance":distance.distance(place1,place2)._Distance__kilometers}




@app.get('/')
def test():
    return "Server start"