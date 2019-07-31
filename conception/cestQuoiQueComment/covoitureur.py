""" le gars il a une voiture il ammene des gens est des fois il est transporté aussi."""
class covoitureur:
    # c'est virtuel, ça ne vaut, c'est des points en fait.
    # mais dans le cas du passager par exemple les sous pourront s'échanger avec du vrai argent de la vie réelle.
    __sous=0 #initialise à 0
    __aUneVoiture=True #sinon t'es même pas un covoitureur

    """tu dors, tu es berçé, tu es emmené par lui, ton covoitureur"""
    def EstEmmenePar(self, lui, trajet):
        Lui.Paye(self, trajet.cout) # c'est pareil que s'il te payait en vrai

    """plus t'emmene de gens, plus c'est rentable car plus il y de personnes qui vont te rendre 'la pareil' ou te donner de l'argent en vrai de la vie en vrai."""
    def Emmene(self, passagers, trajet):
        if(not self.__aUneVoiture):
            return False #Lancer une tuTeFoutDeMaGueuleException

        for passager in passagers:
            passager.EstEmmenePar(self,trajet)
            return True
   
    """tu as payé tes dettes dans la vie en vrai et pour de vrai tu l'as juré sur ta vie"""
    def Paye(self, lui, argent):
        self.__sous, lui.__sous = self.__sous - argent, lui.__sous + argent