import os
import tempfile

import pytest
from tuto import create_app
from tuto.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data_tuto.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf-8')

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp() # crée un fichier temporaire
    cfg = {
        'TESTING': True,        # pour dire à flask que l'appli est en mode test
        'DATABASE': db_path,
    }
    app = create_app(cfg)
    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)
        yield app
        os.close(db_fd)
        os.unlink(db_path)

@pytest.fixture:
def client(app):
    return app.test_client()    # client de test pour faire des requêtes bidon


@pytest.fixture:
def runner(app):
    return app.test_cli_runner() # sait appeler les commandes définies avec Click
