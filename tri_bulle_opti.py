import random
# Fonction utilitaire pour échanger des valeurs à deux indices dans la liste
def swap(A, i, j):
 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
# def nb_ou(mot):
#     compteur = 0
#     for k in range(len(mot)-1):
#         if mot[k]+mot[k+1] == "ou":
#             compteur = compteur +1
#     return compteur
compteurEchange = 0
compteurComparaison = 0
    
# Fonction pour effectuer un tri à bulles sur une liste
def bubbleSort(A):
    global compteurEchange
    global compteurComparaison
    # `len(A)-1` passes
    for k in range(len(A) - 1):
        compteurComparaison += 1
        # les `k` derniers éléments sont déjà triés, donc la boucle interne peut
        # éviter de regarder les derniers `k` éléments
        for i in range(len(A) - 1 - k):
            if A[i] > A[i + 1]:
                swap(A, i, i + 1)
                compteurEchange += 3
                

    return A

performance_bulle_opti = compteurEchange+compteurComparaison


    # l'algorithme peut être terminé si la boucle interne n'a pas fait d'échange


def randomtab (min,max,nbr):
    tab = []
    for i in range(nbr):
        tab.append(random.randint(min,max))
    return tab
liste = [3, 6, 13, 15, 16, 21, 22, 22, 23, 35, 36, 37, 42, 47, 54, 57, 63, 68, 69, 70, 81, 86, 88, 90, 93, 93, 95, 95, 98, 99]
rev=list(reversed(liste))
print(f"{bubbleSort(rev)} , \n la performance est de : {compteurComparaison + compteurEchange}")