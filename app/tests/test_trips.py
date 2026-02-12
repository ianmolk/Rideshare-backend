# app/tests/test_trips.py
import uuid

def test_create_trip(client):
    # create rider
    rider_email = f"rider_{uuid.uuid4().hex[:8]}@test.com"
    r = client.post("/api/v1/auth/register", json={
        "email": rider_email,
        "password": "Password123!",
        "role": "RIDER"
    })
    assert r.status_code == 200
    rider_id = r.json()["id"]

    # create driver user
    driver_email = f"driver_{uuid.uuid4().hex[:8]}@test.com"
    d = client.post("/api/v1/auth/register", json={
        "email": driver_email,
        "password": "Password123!",
        "role": "DRIVER"
    })
    assert d.status_code == 200
    driver_user_id = d.json()["id"]

    # create driver profile
    driver_profile = client.post("/api/v1/drivers", json={
        "user_id": driver_user_id,
        "name": "Test Driver",
        "car_model": "Toyota Camry",
        "plate_number": f"ZZ{uuid.uuid4().hex[:4].upper()}",
        "is_available": True,
        "current_lat": -33.8688,
        "current_lng": 151.2093
    })
    assert driver_profile.status_code == 200
    driver_id = driver_profile.json()["id"]

    # create ride
    ride_res = client.post("/api/v1/rides", json={
        "rider_id": rider_id,
        "pickup_lat": -33.8700,
        "pickup_lng": 151.2060,
        "dropoff_lat": -33.8600,
        "dropoff_lng": 151.2150
    })
    assert ride_res.status_code == 200
    ride_id = ride_res.json()["id"]

    # create trip (adjust body to match your TripCreate schema)
    trip_res = client.post("/api/v1/trips", json={
        "ride_id": ride_id,
        "driver_id": driver_id
    })
    assert trip_res.status_code == 200
