import contexteSocioEconomique

"""du point A au point B"""
class trajet:
    km=120 #km allé retour
    cout=4 #comme ça, c'est tout

    def __init__(self, contexteSocioEconomique):
        self.contexteSocioEconomique = contexteSocioEconomique
        cout = coutParDefaut()

    def coutParDefaut(self):
        return self.contexteSocioEconomique.prixAuKm * self.contexteSocioEconomique.participationPourUnVoyage