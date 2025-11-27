# angle-service/test_angle.py
import pytest
import requests
import time
import threading
from angle_service import app  # ← теперь правильно!

@pytest.fixture(scope="module")
def server():
    thread = threading.Thread(target=app.run, kwargs={"port": 8000})
    thread.daemon = True
    thread.start()
    time.sleep(0.5)
    yield

def test_angle_returns_number(server):
    resp = requests.get("http://127.0.0.1:8000/angle")
    assert resp.status_code == 200
    data = resp.json()
    assert "angle" in data
    assert isinstance(data["angle"], float)

def test_angle_increases_over_time(server):
    angle1 = requests.get("http://127.0.0.1:8000/angle").json()["angle"]
    time.sleep(1.1)
    angle2 = requests.get("http://127.0.0.1:8000/angle").json()["angle"]
    assert angle2 > angle1  # просто больше, без точных градусов
    assert (angle2 - angle1) >= 80  # ~90°/сек