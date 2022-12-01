"""


    PROCEDURE tri_Selection ( Tableau a[1:n])
        POUR i VARIANT DE 1 A n - 1 FAIRE
            TROUVER [j] LE PLUS PETIT ELEMENT DE [i + 1:n];
            ECHANGER [j] ET [i];
    FIN PROCEDURE;


"""


def tri_selection(tableau):
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
    return tableau

tab = [7,2,4,2,5]  
print(tri_selection(tab))   
