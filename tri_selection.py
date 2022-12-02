import random
"""
    initialisation du compteurEchange à 0
    initialisation du compteurComparaison à 0

    PROCEDURE tri_Selection ( Tableau a[1:n])
        informer que compteurEchange est utilisé à l'intérieur et l'extérieur de tri_Selection
        informer que compteurComparaison est utilisé à l'intérieur et l'extérieur de tri_Selection
        POUR i VARIANT DE 1 A n - 1 FAIRE
            TROUVER [j] LE PLUS PETIT ELEMENT DE [i + 1:n];
            ECHANGER [j] ET [i];
            COMPTER L'ECHANGE DE 3 EN 3
            COMPTER LA COMPARAISON DE 1 EN 1

    FIN PROCEDURE;


"""
compteurEchange = 0
compteurComparaison = 0

def tri_selection(tableau):
    global compteurEchange
    global compteurComparaison
    nb = len(tableau)
    for en_cours in range(0,nb):    
        plus_petit = en_cours
        for j in range(en_cours+1,nb) :
            if tableau[j] < tableau[plus_petit] :
                plus_petit = j
        if min is not en_cours :
            temp = tableau[en_cours]
            tableau[en_cours] = tableau[plus_petit]
            tableau[plus_petit] = temp
            compteurEchange += 3
        compteurComparaison += 1
    return tableau

def randomtab (min,max,nbr):
    tab = []
    for i in range(nbr):
        tab.append(random.randint(min,max))
    return tab

print(f"{tri_selection(randomtab(1,100,30))} , \n la performance est de : {compteurComparaison + compteurEchange}")
