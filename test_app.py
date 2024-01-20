import app

def test_hello_world():
    response =app.app.test_client().get('/Hello')
    assert response.status_code == 200
    assert response.data == b'hello'

def test_goodbye():
        response= app.app.test_client().get('/goodbye')
        assert response.status_code == 404

def test_name():
    response =app.app.test_client().get('/name')
    assert response.status_code == 200
    assert response.data == b'Priyansh'