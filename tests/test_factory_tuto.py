from tuto import create_app

def test_config():
    # on n'est pas en mode testing si on ne passe pas 'TESTING': True
    assert not create_app().testing
    # on est en mode testing si on passe 'TESTING': True, ben ouais, forcément
    assert not create_app({'TESTING': True }).testing

def test_hello(client):
    response = client.get('/salut')
    assert response.data = "y a quelqu'un ?"
