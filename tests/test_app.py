import os
import sys

# مسیر روت پروژه (جایی که app.py قرار دارد)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# اضافه کردن مسیر به sys.path
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import app


def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello CI/CD with Python"
