import random
# Fonction utilitaire pour échanger des valeurs à deux indices dans la liste
def swap(A, i, j):
 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp



compteur = 0

    

# Fonction pour effectuer un tri à bulles sur une liste
def bubbleSort(A):
    global compteur;
    # `len(A)-1` passes
    for k in range(len(A) - 1):
 
        # les `k` derniers éléments sont déjà triés, donc la boucle interne peut
        # éviter de regarder les derniers `k` éléments
        for i in range(len(A) - 1 - k):
            if A[i] > A[i + 1]:
                swap(A, i, i + 1)
                compteur += 1
                print(f"Le compteur est {compteur} : {A} ");
                
    return A
    # l'algorithme peut être terminé si la boucle interne n'a pas fait d'échange
 
 
def randomtab (min,max,nbr):
    tab = []
    for i in range(nbr):
        tab.append(random.randint(min,max))
    return tab

print(bubbleSort(randomtab(1,100,30)))
