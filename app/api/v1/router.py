from fastapi import APIRouter
from .auth import router as auth_router
from .rides import router as rides_router
from .drivers import router as drivers_router
from .trips import router as trips_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(rides_router, prefix="/rides", tags=["rides"])
router.include_router(drivers_router, prefix="/drivers", tags=["drivers"])
router.include_router(trips_router, prefix="/trips", tags=["trips"])
