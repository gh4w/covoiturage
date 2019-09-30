#!/usr/bin/env python3
# coding: utf-8


import unittest

import context
from covoiturage.trajet import Trajet
from covoiturage.voyage import Voyage
from covoiturage.contexteSocioEconomique import ContexteSocioEconomique
from covoiturage.covoitureur import Covoitureur

class TestCovoiturage(unittest.TestCase):

    def sumary(self, covoitureurs):
        return ' | '.join(f"{c.say_my_name()} : {c.tirelire()}" for c in covoitureurs)

    def simulerUnVoyage(self, leVoyage,yroule):
        print(f"{yroule.say_my_name()} roule")
        leVoyage.voyager(yroule)
        print(self.sumary(leVoyage._covoitureurs))

    def test(self):
        bill = Covoitureur('bill')
        luc = Covoitureur('hulc')
        dan = Covoitureur('dan vador')
        eco = ContexteSocioEconomique()
        trjt = Trajet(eco)
        tousLesCovoits = [bill,luc,dan]
        leVoyage = Voyage(tousLesCovoits,trjt)
        print(f"au départ : {self.sumary(tousLesCovoits)}")

        self.simulerUnVoyage(leVoyage,dan)
        self.simulerUnVoyage(leVoyage,luc)
        self.simulerUnVoyage(leVoyage,bill)
        print("derniere etape tout le monde est à 0")
        print()

        self.simulerUnVoyage(leVoyage,dan)
        self.simulerUnVoyage(leVoyage,luc)
        sentance = f"hé bien mon petit {leVoyage.qui_roule().say_my_name()} c'est toi qui t'y colle pour le prochain voyage."
        print(sentance)

if __name__ == '__main__':
    unittest.main()
