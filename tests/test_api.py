from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "workout-recommendation-api"}

def test_recommend_endpoint():
    payload = {
        "user_info": {
            "age": 28,
            "gender": "female"
        },
        "goals": {
            "current_weight_kg": 65.0,
            "target_weight_kg": 60.0,
            "target_muscle_mass_kg": 2.0
        }
    }
    response = client.post("/api/v1/recommend", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "exercises" in data
    assert len(data["exercises"]) > 0
