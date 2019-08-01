class Covoitureur:
    """ le gars il a une voiture il ammene des gens est des fois il est transporté aussi."""

    def __init__(self, nom):
        """ctor"""
        self._nom = nom
        # c'est virtuel, ça ne vaut, c'est des points en fait.
        # mais dans le cas du passager par exemple les sous pourront s'échanger avec du vrai argent de la vie réelle.
        self._sous=0 #initialise à 0
        self.a_une_voiture=True #sinon t'es même pas un covoitureur

    def estEmmenePar(self, lui, trajet):
        """tu dors, tu es berçé, tu es emmené par lui, ton covoitureur"""
        Lui.paye(self, trajet.cout()) # c'est pareil que s'il te payait en vrai

    def emmene(self, passagers, trajet):
        """plus t'emmene de gens, plus c'est rentable car plus il y de personnes qui vont te rendre 'la pareil' ou te donner de l'argent en vrai de la vie en vrai."""
        if(not self.a_une_voiture):
            return False #Lancer une tuTeFoutDeMaGueuleException

        for passager in passagers:
            passager.estEmmenePar(self,trajet)
            return True
   
    def paye(self, lui, argent):
        """tu as payé tes dettes dans la vie en vrai et pour de vrai tu l'as juré sur ta vie"""
        self._sous, lui._sous = self._sous - argent, lui._sous + argent

    def say_my_name(self):
        """ On reconaitra la réference au boxeur célèbre j'espère."""
        return self._nom

    def tirelire(self):
        """ expose l'argent acumulé."""
        return self._sous
        