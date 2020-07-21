import json


def test_health(test_app):
    client = test_app.test_client()
    resp = client.get('/health')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'UP!' in data['message']
    assert 'success' in data['status']