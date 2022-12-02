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

def randomtab (min,max,nbr):
    tab = []
    for i in range(nbr):
        tab.append(random.randint(min,max))
    return tab

print(f"{tri_insertion(randomtab(1,100,30))} , \n la performance est de : {compteurComparaison + compteurEchange}")

    