# coding: utf-8
from trajet import Trajet
from voyage import Voyage
from contexteSocioEconomique import ContexteSocioEconomique
from covoitureur import Covoitureur

def sumary(covoitureurs):
    return ' | '.join(f"{c.say_my_name()} : {c.tirelire()}" for c in covoitureurs)

def simulerUnVoyage(leVoyage,yroule):
    print(f"{yroule.say_my_name()} roule")
    leVoyage.voyager(yroule)
    print(sumary(leVoyage._covoitureurs))

def test():
    bill = Covoitureur('bill')
    luc = Covoitureur('hulc')
    dan = Covoitureur('dan vador')
    eco = ContexteSocioEconomique()
    trjt = Trajet(eco)
    tousLesCovoits = [bill,luc,dan]
    leVoyage = Voyage(tousLesCovoits,trjt)
    print(f"au départ : {sumary(tousLesCovoits)}")

    simulerUnVoyage(leVoyage,dan)
    simulerUnVoyage(leVoyage,luc)
    simulerUnVoyage(leVoyage,bill)
    print("derniere etape tout le monde est à 0")
    print()

    simulerUnVoyage(leVoyage,dan)
    simulerUnVoyage(leVoyage,luc)
    sentance = f"hé bien mon petit {leVoyage.qui_roule().say_my_name()} c'est toi qui t'y colle pour le prochain voyage."
    print(sentance)
