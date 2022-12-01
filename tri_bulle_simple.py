import random
"""
    PROCEDURE tri_bulle normal ( TABLEAU a[1:n])
    passage ← 0
    REPETER
        permut ← FAUX
        POUR i VARIANT DE 1 A n - 1 - passage FAIRE
            SI a[i] > a[i+1] ALORS
                echanger a[i] ET a[i+1]
                permut ← VRAI
            FIN SI
        FIN POUR
        passage ← passage + 1
    TANT QUE permut = VRAI

"""

compteurEchange = 0
compteurComparaison = 0

tab = [0,3,2,1]
def tri_bulle(tableau):
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
def randomtab (min,max,nbr):
    tab = []
    for i in range(nbr):
        tab.append(random.randint(min,max))
    return tab

print(f"{tri_bulle(randomtab(1,100,30))} , \n la performance est de : {compteurComparaison + compteurEchange}")
