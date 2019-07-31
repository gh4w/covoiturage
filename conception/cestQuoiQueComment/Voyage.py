import Covoitureur

"""c'est partit pour le road trip"""
class Voyage:
    _covoitureurs
    _trajet

    def __init__(self, covoitureurs, trajet):
        _covoitureurs = covoitureurs
        _trajet = trajet

    """ Choisir qui roule parmis les covoitureurs."""
    def qui_roule(self, covoitureurs = _covoitureurs):
        minimumDeSous = min(c.Tirelire for c in covoitureurs if c.)
        return next(c for c in covoitureurs if c.Tirelire = minimumDeSous)

    """Le voyage est effectué, on fait les comptes"""
    def voyager(self, conducteur, covoitureurs, trajet = _trajet):
        conducteur.Emmene(covoitureurs, trajet)
