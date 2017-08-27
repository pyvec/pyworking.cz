def test_get_index():
    from pyworking_cz import app
    with app.test_client() as c:
        resp = c.get('/')
        assert resp.status_code == 200
        assert b'PyWorking' in resp.data
