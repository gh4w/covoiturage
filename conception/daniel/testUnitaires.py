# coding: utf-8
from trajet import Trajet
from voyage import Voyage
from contexteSocioEconomique import ContexteSocioEconomique
from covoitureur import Covoitureur

def test():

    bill = Covoitureur('bill')
    luc = Covoitureur('hulc')
    dan = Covoitureur('dan vador')
    eco = ContexteSocioEconomique()
    trjt = Trajet(eco)
    tousLesCovoits = [bill,luc,dan]
    leVoyage = Voyage(tousLesCovoits,trjt)

    leVoyage.voyager(dan)
    print(f"dan :  {dan.tirelire()} | luc : {luc.tirelire()} | bill : {bill.tirelire()}")

    leVoyage.voyager(luc)
    print(f"dan :  {dan.tirelire()} | luc : {luc.tirelire()} | bill : {bill.tirelire()}")

    print(leVoyage.qui_roule())
