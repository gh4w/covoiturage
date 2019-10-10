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

tuto django: https://docs.djangoproject.com/en/2.2/intro/tutorial01/
tuto django-rest: https://www.django-rest-framework.org/tutorial/quickstart/
