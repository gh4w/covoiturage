
class Voyage:
    """c'est partit pour le road trip"""

    def __init__(self, covoitureurs, trajet):
        self._covoitureurs = covoitureurs
        self._trajet = trajet

    def qui_roule(self):
        """ Choisir qui roule parmis les covoitureurs."""
        minimumDeSous = min(c._sous for c in self._covoitureurs if c.a_une_voiture)
        return next(c for c in self._covoitureurs if c.tirelire() == minimumDeSous)

    def voyager(self, conducteur):
        """Le voyage est effectué, on fait les comptes"""
        conducteur.emmene(self._covoitureurs, self._trajet)
