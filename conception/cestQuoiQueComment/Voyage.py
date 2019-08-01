import Covoitureur

class Voyage:
    """c'est partit pour le road trip"""

    def __init__(self, covoitureurs, trajet):
        self._covoitureurs = covoitureurs
        self._trajet = trajet

    def qui_roule(self, covoitureurs):
        """ Choisir qui roule parmis les covoitureurs."""
        minimumDeSous = min(c.tirelire for c in covoitureurs if c.a_une_voiture)
        return next(c for c in covoitureurs if c.tirelire == minimumDeSous)

    def voyager(self, conducteur, covoitureurs, trajet):
        """Le voyage est effectué, on fait les comptes"""
        conducteur.emmene(covoitureurs, trajet)
