"""


    PROCEDURE tri_Insertion ( Tableau a[1:n])
        POUR i VARIANT DE 2 A n FAIRE
            INSERER a[i] à sa place dans a[1:i-1];
    FIN PROCEDURE;


"""




def tri_insertion(tableau):
    for i in range(1,len(tableau)):
        en_cours = tableau[i]
        j = i
        #décalage des éléments du tableau }
        while j>0 and tableau[j-1]>en_cours:
            tableau[j]=tableau[j-1]
            j = j-1
        #on insère l'élément à sa place
        tableau[j]=en_cours
    return tableau

        
tab = [7,2,4,2,5]  
print(tri_insertion(tab))   
   
    