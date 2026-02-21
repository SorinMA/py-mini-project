from app.utils import SuperManager

def test_math_division():
    manager = SuperManager()
    assert manager.divide(10, 2) == "[SUCCESS] 5.0"
    assert manager.divide(10, 0) == "[FAILURE]"

def test_calculate_route(client):
    response = client.get('/calculate?a=10&b=2')
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == "[SUCCESS] 5.0"
    assert "time" in data