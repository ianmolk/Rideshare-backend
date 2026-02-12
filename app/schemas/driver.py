from pydantic import BaseModel

class DriverCreate(BaseModel):
    user_id: int
    current_lat: float
    current_lng: float


class DriverOut(BaseModel):
    id: int
    user_id: int
    current_lat: float | None = None
    current_lng: float | None = None
    is_available: bool


    class Config:
        from_attributes = True

    

