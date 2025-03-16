carre_mag = [4, 14, 15, 1],[9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]
carre_pas_mag = [ligne[:] for ligne in carre_mag]
carre_pas_mag[-1][-2] = 7
print(carre_pas_mag)

def afficheCarre(carre:list)->list:
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for ligne in carre:
        print(ligne)

afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)

def testLignesEgales(carre:list)-> int:
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    x = sum(carre[0])
    for ligne in carre:
        if sum(ligne) != x:
            return -1
    return x

print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))

def testColonnesEgales(carre:list)->int:
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    C1 = [ligne[0] for ligne in carre]
    x = sum(C1)
    for n_colonne in range(1, len(carre)):
        colonne = [ligne[n_colonne] for ligne in carre]
        if sum(colonne) != x:
            return -1
    return x

print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))

def testDiagonalesEgales(carre:list)->int:
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    D1 = [carre[i][i] for i in range(len(carre))]
    D2 = [carre[i][len(carre)-i-1] for i in range(len(carre))]
    x = sum(D1)
    if sum(D2) != x:
        return -1
    else:
        return x

print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag)) 

def estCarreMagique(carre:list)->bool:
    """ Renvoie True si c'est un carre magique et False sinon"""
    return testLignesEgales(carre) == testColonnesEgales(carre) and testLignesEgales(carre) == testLignesEgales(carre) and testLignesEgales(carre) != -1

print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))

def estNormal(carre:list)-> bool:
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    

print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))