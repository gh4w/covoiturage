# Installation de l'environnement de dev sous Powershell

1. cloner le dépôt
    ```ps1
    git clone https://github.com/gh4w/covoiturage.git
    ```
2. créer un environnement virtuel à la racine du dépôt
    ```ps1
    python -m venv env
    ```
3. Activer l'environnement virtuel
    ```ps1
    ./env/Scripts/Activate.ps1
    ```
4. Installer les dépendances
    ```ps1
    pip install -r ./src/requirements.txt
    ```
## Liens

flask: http://flask.palletsprojects.com/en/1.1.x/
flask: mise en place des tests: http://flask.palletsprojects.com/en/1.1.x/testing/

## lancer le serveur de dev en local:

```ps1
$env:FLASK_APP="karpoule"
$env:FLASK_ENV="development"
flask run
```

## déployer sur heroku:

```ps1
git push heroku master
```

## TODO

- logs en dev et en prod: flask -> gunicorn -> heroku
- flask & heroku: déployer une bdd

