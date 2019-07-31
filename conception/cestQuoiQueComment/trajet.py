import contexteSocioEconomique

"""du point A au point B"""
class Trajet:
    _contexteSocioEconomique
    km=120 #km allé retour
    participation=1/3

    """ctor"""
    def __init__(self, contexteSocioEconomique):
        self._contexteSocioEconomique = contexteSocioEconomique

    """ Combien tu paye pour être transporté sur ce voyage."""
    def cout(self):
        return self.cout_total() * self.participation

    """ Combien ça coute en vrai, un voyage, dans notre contexte socio economique."""
    def cout_total(self):
        return self._contexteSocioEconomique.prixAuKm * self.km

    """ En fait on a décidé des sous que doit donner un passager pour un voyage."""
    def redefinir_la_participation(self, cout):
        self.participation = self.cout_total() / cout