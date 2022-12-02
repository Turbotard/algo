import random
"""
    initialisation du compteurEchange à 0
    initialisation du compteurComparaison à 0
    PROCEDURE tri_bulle normal ( TABLEAU a[1:n])
    informer que compteurEchange est utilisé à l'intérieur et l'extérieur de tri_Selection
    informer que compteurComparaison est utilisé à l'intérieur et l'extérieur de tri_Selection
    passage ← 0
    REPETER
        permut ← FAUX
        POUR i VARIANT DE 1 A n - 1 - passage FAIRE
            SI a[i] > a[i+1] ALORS
                echanger a[i] ET a[i+1]
                permut ← VRAI
                COMPTER L'ECHANGE DE 3 EN 3
            FIN SI
            COMPTER LA COMPARAISON DE 1 EN 1
        FIN POUR
        passage ← passage + 1
    TANT QUE permut = VRAI

"""

compteurEchange = 0
compteurComparaison = 0

tab = [0,3,2,1]
def tri_bulle_simple(tableau):
    global compteurEchange
    global compteurComparaison
    permutation = True
    passage = 0
    while permutation == True:
        permutation = False
        passage = passage + 1
        for en_cours in range(0, len(tableau) - passage):
            if tableau[en_cours] > tableau[en_cours + 1]:
                permutation = True
                # On echange les deux elements
                tableau[en_cours], tableau[en_cours + 1] = \
                tableau[en_cours + 1],tableau[en_cours]
                compteurEchange += 3
        compteurComparaison += 1
    return tableau  

performance_bulle_simple = compteurComparaison + compteurEchange
def randomtab (min,max,nbr):
    tab = []
    for i in range(nbr):
        tab.append(random.randint(min,max))
    return tab
liste = [3, 6, 13, 15, 16, 21, 22, 22, 23, 35, 36, 37, 42, 47, 54, 57, 63, 68, 69, 70, 81, 86, 88, 90, 93, 93, 95, 95, 98, 99]
rev=list(reversed(liste))
print(f"{tri_bulle_simple(rev)} , \n la performance est de : {compteurComparaison + compteurEchange}")
