import contexteSocioEconomique

"""du point A au point B"""
class trajet:
    km=120 #km allé retour
    cout=4 #comme ça, c'est tout

    """ctor"""
    def __init__(self, contexteSocioEconomique):
        self.contexteSocioEconomique = contexteSocioEconomique
        cout = coutParDefaut()

    """ Combien tu paye pour être transporté sur ce voyage."""
    def coutParDefaut(self):
        return self.prixDuVoyage() * self.contexteSocioEconomique.participationPourUnVoyage

    """ Combien ça coute en vrai, un voyage, dans notre contexte socio economique."""
    def prixDuVoyage(self):
        return self.contexteSocioEconomique.prixAuKm * self.km

    """ En fait on a décidé des sous que doit donner un passager pour un voyage."""
    def redefinirLaParticipation(self, cout):
        self.participationPourUnVoyage = self.prixDuVoyage() / cout