from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base


class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)

    ride_request_id = Column(Integer, ForeignKey("ride_requests.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=False)

    status = Column(String, nullable=False, default="ASSIGNED")
