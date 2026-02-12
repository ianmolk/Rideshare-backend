from pydantic import BaseModel



class RideCreate(BaseModel):
    rider_id: int
    pickup_lat: float
    pickup_lng: float 
    dropoff_lat: float
    dropoff_lng: float

class RideOut(BaseModel):
    id: int
    rider_id: int
    pickup_lat: float
    pickup_lng: float
    dropoff_lat: float
    dropoff_lng: float
    status: str

class Config:
        from_attributes = True
