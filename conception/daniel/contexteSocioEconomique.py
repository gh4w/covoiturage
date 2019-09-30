
class ContexteSocioEconomique:

    def __init__(self, litreAuCent = 8, prixAuLitre = 1.4):
        self._litreAuCent = litreAuCent
        self._prixAuLitre = prixAuLitre

    def prixAuKm(self):
        return self._litreAuCent*self._prixAuLitre/100