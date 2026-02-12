from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.base import Base

class RideRequest(Base):
    __tablename__ = "ride_requests"

    id = Column(Integer, primary_key=True, index=True)

    rider_id= Column(Integer, ForeignKey("users.id"), nullable=False)

    pickup_lat = Column(Float, nullable=False)
    pickup_lng = Column(Float, nullable=False)

    dropoff_lat = Column(Float, nullable=False)
    dropoff_lng = Column(Float, nullable = False)

    status = Column(String, nullable=False, default="REQUESTED")