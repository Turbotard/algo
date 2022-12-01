# Fonction utilitaire pour échanger des valeurs à deux indices dans la liste
def swap(A, i, j):
 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 
 
# Fonction pour effectuer un tri à bulles sur une liste
def bubbleSort(A):
 
    # `len(A)-1` passes
    for k in range(len(A) - 1):
 
        # les `k` derniers éléments sont déjà triés, donc la boucle interne peut
        # éviter de regarder les derniers `k` éléments
        for i in range(len(A) - 1 - k):
            if A[i] > A[i + 1]:
                swap(A, i, i + 1)
    return A
    # l'algorithme peut être terminé si la boucle interne n'a pas fait d'échange
 
 
tab = [0,2,1,3,4,1]
print(bubbleSort(tab))
