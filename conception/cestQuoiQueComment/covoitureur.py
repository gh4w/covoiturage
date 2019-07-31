""" le gars il a une voiture il ammene des gens est des fois il est transporté aussi."""
class Covoitureur:
    # c'est virtuel, ça ne vaut, c'est des points en fait.
    # mais dans le cas du passager par exemple les sous pourront s'échanger avec du vrai argent de la vie réelle.
    _sous=0 #initialise à 0
    a_une_voiture=True #sinon t'es même pas un covoitureur
    _nom

    """ctor"""
    def __init__(self, nom):
        _nom = nom

    """tu dors, tu es berçé, tu es emmené par lui, ton covoitureur"""
    def estEmmenePar(self, lui, trajet):
        Lui.paye(self, trajet.cout()) # c'est pareil que s'il te payait en vrai

    """plus t'emmene de gens, plus c'est rentable car plus il y de personnes qui vont te rendre 'la pareil' ou te donner de l'argent en vrai de la vie en vrai."""
    def emmene(self, passagers, trajet):
        if(not self.a_une_voiture):
            return False #Lancer une tuTeFoutDeMaGueuleException

        for passager in passagers:
            passager.estEmmenePar(self,trajet)
            return True
   
    """tu as payé tes dettes dans la vie en vrai et pour de vrai tu l'as juré sur ta vie"""
    def paye(self, lui, argent):
        self._sous, lui._sous = self._sous - argent, lui._sous + argent

    """ On reconaitra la réference au boxeur célèbre j'espère."""
    def say_my_name(self):
        return self._nom

    """ expose l'argent acumulé."""
    def tirelire(self):
        return self._sous
        