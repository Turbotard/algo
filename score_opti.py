# Import des quatres fichier dans celui ci pour faire une liste du plus perfmormant au moins performant
from tri_bulle_opti import*
from tri_bulle_simple import*
from tri_insertion import*
from tri_selection import*


nombrebatterie=int(input("entrer un nombre entre 1 et 100 : "))
classement = [performance_bulle_opti, performance_bulle_simple, performance_insertion, performance_selection]
def Classement(classement):
    for k in range(len(classement) - 1):
        for i in range(len(classement) - 1 - k):
                    if classement[i] > classement[i + 1]:
                        swap(classement, i, i + 1)
    return classement

Classement()




