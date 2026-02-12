from pydantic import BaseModel

class TripCreate(BaseModel):
    ride_request_id: int
    driver_id: int

class TripOut(BaseModel):
    id: int
    ride_request_id: int
    driver_id: int 
    status: str

    class Config:
        from_attributes=True
        