import pytest
from app.main import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_health(client):
    res = client.get('/')
    assert res.status_code == 200

def test_shorten_and_redirect(client):
    res = client.post('/api/shorten', json={'url': 'https://example.com'})
    assert res.status_code == 201
    data = res.get_json()
    code = data['short_code']

    redirect_res = client.get(f'/{code}', follow_redirects=False)
    assert redirect_res.status_code == 302

    stats_res = client.get(f'/api/stats/{code}')
    assert stats_res.status_code == 200
    stats = stats_res.get_json()
    assert stats['clicks'] == 1
