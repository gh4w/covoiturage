# contexte

## 27/08/2019

plusieurs personnes font du covoiturage:
- pour faire un trajet entre un point de départ et un point d'arrivée 
- les points de départ et d'arrivée ont un nom, genre "Parking du Leclerc" et "Ma petite entreprise"
- pour le trajet il y a une heure de départ
- une durée estimée aussi ? => heure estimée d'arrivée ?
- les personnes ont un rôle: conducteur ou passager
- y a aussi une bagnole: en général c'est celle du conducteur
- le trajet fait un certain nombre de kilomètres
- distinguer entre un trajet prévu, qui change pas, et le trajet réel:
    - qui se fait un jour donné, à une date donnée, a une heure de départ et d'arrivée => copier sur Waze
    - le trajet c'est une classe, et y a des instances de trajet

```python
def exemple():

    i = Itineraire()
    i.libelle = "de Vaucanson à ICE"
    i.depart = "Parking du lycée Vaucanson"
    i.arrive = "Parking de ICE"
    i.distance = 62 # en km

    t = Trajet()
    t.itineraire = i
    t.date_depart = "28/8/2019"
    t.heure_depart_prevue = "7h30"
    t.conducteur = "daniel"
    t.passagers = ["luc", "jules"]

```
