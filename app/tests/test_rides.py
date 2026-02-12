# app/tests/test_rides.py
import uuid

def test_create_and_get_ride(client):
    email = f"rider_{uuid.uuid4().hex[:8]}@test.com"

    r = client.post("/api/v1/auth/register", json={
        "email": email,
        "password": "Password123!",
        "role": "RIDER"
    })
    assert r.status_code == 200
    rider_id = r.json()["id"]

    # create ride
    res = client.post("/api/v1/rides", json={
        "rider_id": rider_id,
        "pickup_lat": -33.8700,
        "pickup_lng": 151.2060,
        "dropoff_lat": -33.8600,
        "dropoff_lng": 151.2150
    })
    assert res.status_code == 200
    ride_id = res.json()["id"]

    # get ride (adjust path if yours is different)
    get_res = client.get(f"/api/v1/rides/{ride_id}")
    assert get_res.status_code == 200
