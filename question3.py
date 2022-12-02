import random
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
            ls = [random.randint(0, 100) for _ in range(i)]
            acc += bubbleSort(ls)
        print(i, acc / nbr *0.1)
stat(10, 20, 5, 500)