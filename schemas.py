
from pydantic import BaseModel



class AZA_geocode(BaseModel):
    pin1:str
    pin2:str
    
class geocode_res(BaseModel):
    distance:int
    class Config:
         orm_mode = True