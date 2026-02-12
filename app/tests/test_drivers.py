# app/tests/test_drivers.py
import uuid

def test_create_driver(client):
    email = f"driver_{uuid.uuid4().hex[:8]}@test.com"

    # register driver user
    r = client.post("/api/v1/auth/register", json={
        "email": email,
        "password": "Password123!",
        "role": "DRIVER"
    })
    assert r.status_code == 200
    user_id = r.json()["id"]

    # create driver profile using returned id
    res = client.post("/api/v1/drivers", json={
        "user_id": user_id,
        "name": "Bob Driver",
        "car_model": "Toyota Camry",
        "plate_number": f"ABC{uuid.uuid4().hex[:3].upper()}",
        "is_available": True,
        "current_lat": -33.8688,
        "current_lng": 151.2093
    })
    assert res.status_code == 200
    data = res.json()
    assert data["user_id"] == user_id
