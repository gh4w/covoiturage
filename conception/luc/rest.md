# notes sur la conception d'une api REST

## le problème de plusieurs appels vs un seul appel

imaginons qu'on ait une api rest découpée proprement en fonction du domaine, par exemple:

- `GET http://mon.serveur/api/utilisateurs` renvoie la liste des utilisateurs
- `GET http://mon.serveur/api/utilisateurs/1234` renvoie les données de l'utilisateurs 1234
- `GET http://mon.serveur/api/itinéraires` renvoie la liste des itinéraires existants  (par ex, 
- `GET http://mon.serveur/api/itinéraires/1234` renvoie les données de l'itinéraire n°1234 (ville de départ, d'arrivée, etc...)

On a maintenant un écran qui affiche un formulaire de création d'un nouveau trajet.  
L'écran permet de sélectionner des utilisateurs dans la liste des utilisateurs, l'itinéraire dans la liste des itinéraires, 
de fixer la date du trajet, etc, etc...

Pour afficher cet écran est-ce qu'on fait:

- 2 appels GET: 1 pour récupérer la liste des utilisateurs, 1 pour la liste des trajets
- 1 seul appel GET, qui renvoie un objet qui contient à la fois la liste des utilisateurs + la liste des trajets ?

Quand on a fini de remplir le formulaire, avec la date du trajet, etc... est-ce qu'on fait:

- 1 seul requete POST qui envoie toutes les informations d'un coup pour créer le trajet ?
- plusieurs appels POST, 1 par ressource à modifier pour que le trajet soit créé ?

De manière général, un formulaire affiché à l'utilisateur combine plusieurs ressources, qu'il peut modifier indépendamment ou toutes à la fois.  
Est-ce qu'il faut prévoir une "ressource" spéciale qui représente *ce formulaire* dans l'api, du genre `http://mon.serveur/api/creation-trajet` sur lequel on peut faire 
un GET et un POST, ou bien c'est le navigateur qui compose la page en allant taper sur les ressources pour les afficher, puis qui dispatche les POST entre les différentes ressources ?






