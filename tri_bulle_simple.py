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
tab = [0,3,2,1]
def tri_bulle(tableau):
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
    return tableau  
tab = [7,2,4,2,5]  
print(tri_bulle(tab))   

