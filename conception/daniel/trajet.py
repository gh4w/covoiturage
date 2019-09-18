import ContexteSocioEconomique

class Trajet:
    """du point A au point B"""

    def __init__(self, contexteSocioEconomique):
        """ctor"""
        self._contexteSocioEconomique = contexteSocioEconomique
        self.km = 120
        self.participation=1/3

    def cout(self):
        """ Combien tu paye pour être transporté sur ce voyage."""
        return self.cout_total() * self.participation

    def cout_total(self):
        """ Combien ça coute en vrai, un voyage, dans notre contexte socio economique."""
        return self._contexteSocioEconomique.prixAuKm * self.km

    def redefinir_la_participation(self, cout):
        """ En fait on a décidé des sous que doit donner un passager pour un voyage."""
        self.participation = self.cout_total() / cout