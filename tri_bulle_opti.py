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
 
        # les `k` derniers éléments sont déjà triés, donc la boucle interne peut
        # éviter de regarder les derniers `k` éléments
        for i in range(len(A) - 1 - k):
            if A[i] > A[i + 1]:
                swap(A, i, i + 1)
                compteurEchange += 3
                compteurComparaison += 1
                print(f"{compteurComparaison}/ Le compteurEchange est {compteurEchange} : {A} \n ")
             
                
    return A
    # l'algorithme peut être terminé si la boucle interne n'a pas fait d'échange
 
 
 
def randomtab (min,max,nbr):
    tab = []
    for i in range(nbr):
        tab.append(random.randint(min,max))
    return tab

print(bubbleSort(randomtab(1,100,30)))

def suite(ls, fin):
    while(ls[-1] < fin):
        ls.append(ls[-1] + ls[-2])
    return ls

def reverse(ls, ordre):
    ls[::ordre], ls[::-ordre] = ls[::-ordre], ls[::ordre]


def swap(A, i, j):
 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# Fonction pour effectuer un tri à bulles sur une liste
def bubbleSort(A):
    compteurEchange = 0
    compteurComparaison = 0
    # `len(A)-1` passes
    for k in range(len(A) - 1):
 
        # les `k` derniers éléments sont déjà triés, donc la boucle interne peut
        # éviter de regarder les derniers `k` éléments
        for i in range(len(A) - 1 - k):
            if A[i] > A[i + 1]:
                A[i], A[i+1] = A[i+1], A[i]
                compteurEchange += 3
                compteurComparaison += 1
    return compteurEchange + compteurComparaison


def stat(min, max, step, nbr):
    for i in range(min, max + step, step):
        acc = 0
        for n in range(nbr):
            ls = [rd.randint(0, 100) for _ in range(i)]
            acc += bubbleSort(ls)
        print(i, acc / nbr *0.1)
stat(10, 20, 5, 500)
