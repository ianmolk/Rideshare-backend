from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from app.db.base import Base


class Driver(Base):
    __tablename__="drivers"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)

    current_lat = Column(Float, nullable=True)
    current_lng = Column(Float, nullable= True)

    is_available = Column(Boolean, nullable=False, default=True)
