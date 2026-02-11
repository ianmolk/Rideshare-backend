from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.models.trip import Trip
from app.schemas.trip import TripCreate, TripOut

router = APIRouter()


@router.post("", response_model=TripOut)
def create_trip(payload: TripCreate, db: Session = Depends(get_db)):
    trip= Trip(
        ride_request_id=payload.ride_request_id,
        driver_id=payload.driver_id,
        status="ASSIGNED",
    )
    db.add(trip)
    db.commit()
    db.refresh(trip)
    return trip

@router.get("/{trip_id}", response_model=TripOut)
def get_trip(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip
