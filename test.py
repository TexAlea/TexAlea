
from random import *

class listeAleatoire(list) :
    """Classe définissant un objet list étendu par une méthode _remplir pour un remplissage aléatoire de nombres lors de l'instanciation.
    Les nombres ajoutés à la liste sont compris entre a et b entiers, avec un incrément à préciser.
    Facultatif : des valeurs à supprimer (par exemple 0), la longueur de la liste à générer.
    """
    def __init__(self,a,b,increment=1,listeASupprimer=[],nbreValeursSouhaitees=10) :
        #list.__init__(self)
        #self.append(10)
        nombreDeValeurs = int((b-a)/increment+1)
        if nombreDeValeurs >= 2 : # en dessous de deux valeurs, on ne remplit pas.
            if nombreDeValeurs == 2 : # s'il n'y a que deux valeurs, on utilise un alea réel
                for i in range(nbreValeursSouhaitees) :
                    super().append(choice([a,b]))
            else :
                while len(self) < nbreValeursSouhaitees :
                    L = []
                    for i in range(a,b+1,increment) :
                        L.append(i)
                    shuffle(L)
                    super().extend(L)
        else :
            print("Nombre de valeurs incorrect : ", nombreDeValeurs)
                    

N3 = listeAleatoire(3,8,2)
print(N3)





