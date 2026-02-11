from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.models.driver import Driver
from app.schemas.driver import DriverCreate, DriverOut

router = APIRouter()


@router.post("", response_model=DriverOut)
def create_driver(payload: DriverCreate, db: Session = Depends(get_db)):
    driver = Driver(
        user_id=payload.user_id,
        current_lat=payload.current_lat,
        current_lng=payload.current_lng,
        is_available=True,
    )
    db.add(driver)
    db.commit()
    db.refresh(driver)
    return driver

@router.get("", response_model=list[DriverOut])
def list_drivers(db: Session = Depends(get_db)):
    return db.query(Driver).all()


@router.get("/{driver_id}", response_model=DriverOut)
def get_driver(driver_id: int, db: Session = Depends(get_db)):
    driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver