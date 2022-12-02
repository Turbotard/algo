import random 
"""
    initialisation du compteurEchange à 0
    initialisation du compteurComparaison à 0

    PROCEDURE tri_Insertion ( Tableau a[1:n])
        informer que compteurEchange est utilisé à l'intérieur et l'extérieur de tri_Selection
        informer que compteurComparaison est utilisé à l'intérieur et l'extérieur de tri_Selection
        POUR i VARIANT DE 2 A n FAIRE
            INSERER a[i] à sa place dans a[1:i-1];
            COMPTER L'ECHANGE DE 3 EN 3
            COMPTER LA COMPARAISON DE 1 EN 1
    FIN PROCEDURE;


"""
compteurEchange = 0
compteurComparaison = 0

def tri_insertion(tableau):
    global compteurEchange
    global compteurComparaison
    for i in range(1,len(tableau)):
        en_cours = tableau[i]
        j = i
        compteurComparaison += 1
        #décalage des éléments du tableau }
        while j>0 and tableau[j-1]>en_cours:
            tableau[j]=tableau[j-1]
            j = j-1
            compteurEchange += 3
        #on insère l'élément à sa place
        tableau[j]=en_cours
    
    return tableau
performance_insertion = compteurComparaison + compteurEchange

def randomtab (min,max,nbr):
    tab = []
    for i in range(nbr):
        tab.append(random.randint(min,max))
    return tab
liste = [3, 6, 13, 15, 16, 21, 22, 22, 23, 35, 36, 37, 42, 47, 54, 57, 63, 68, 69, 70, 81, 86, 88, 90, 93, 93, 95, 95, 98, 99]
rev=list(reversed(liste))
print(f"{tri_insertion(rev)} , \n la performance est de : {compteurComparaison + compteurEchange}")

    