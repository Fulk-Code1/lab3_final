# test_angle.py
import pytest
import requests
import time

def test_angle_returns_valid_json():
    resp = requests.get("http://localhost:8000/angle")
    assert resp.status_code == 200
    data = resp.json()
    assert "angle" in data
    assert isinstance(data["angle"], float)

def test_angle_increases():
    angle1 = requests.get("http://localhost:8000/angle").json()["angle"]
    time.sleep(1.1)
    angle2 = requests.get("http://localhost:8000/angle").json()["angle"]
    diff = (angle2 - angle1) % 360
    assert diff > 80  # ~90 градусов в секунду