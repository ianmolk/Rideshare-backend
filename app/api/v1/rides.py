from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.models.ride_request import RideRequest
from app.schemas.ride import RideCreate, RideOut

router = APIRouter()


@router.post("", response_model=RideOut)
def create_ride(payload: RideCreate, db: Session = Depends(get_db)):
    ride = RideRequest(
        rider_id=payload.rider_id,
        pickup_lat=payload.pickup_lat,
        pickup_lng=payload.pickup_lng,
        dropoff_lng=payload.dropoff_lng,
        dropoff_lat=payload.dropoff_lat,
        status="REQUESTED",
    )
    db.add(ride)
    db.commit()
    db.refresh(ride)
    return ride


@router.get("/{ride_id}", response_model=RideOut)
def get_ride(ride_id: int, db: Session = Depends(get_db)):
    ride = db.query(RideRequest).filter(RideRequest.id == ride.id).first()
    if ride is None:
        raise HTTPException(status_code=404, detail="RIde not found")
    return ride