import Covoitureur

class Voyage:
"""c'est partit pour le road trip"""

    def __init__(self, covoitureurs, trajet):
        self._covoitureurs = covoitureurs
        self._trajet = trajet

    def qui_roule(self, covoitureurs = _covoitureurs):
        """ Choisir qui roule parmis les covoitureurs."""
        minimumDeSous = min(c.Tirelire for c in covoitureurs if c.)
        return next(c for c in covoitureurs if c.Tirelire = minimumDeSous)

    def voyager(self, conducteur, covoitureurs, trajet = _trajet):
        """Le voyage est effectué, on fait les comptes"""
        conducteur.Emmene(covoitureurs, trajet)
