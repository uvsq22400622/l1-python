def syracuse(n:int)-> list:
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    r = [n]
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = (n*3)+1
        r.append(n)
    return r

print(syracuse(3))

def testeConjecture(n_max:int)-> bool:
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    for i in range(1, n_max+1):
        syracuse(i)
    return True

print(testeConjecture(10000))

def tempsVol(n:int)-> int:
    """ Retourne le temps de vol de n """
    return len(syracuse(n))-1

print("Le temps de vol de", 3, "est", tempsVol(3))

def tempsVolListe(n_max:int)->list:
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    return [tempsVol(i) for i in range(1, n_max+1)]

print(tempsVolListe(100))

liste_temps = tempsVolListe(10000)
temps_max = max(liste_temps)
print("L'entier",liste_temps.index(temps_max)+1, "a le plus grand temps de vol égal à", temps_max)

def altMax(n:int)-> int:
    """Retourne l'altitude max d'un entier n."""
    return max(syracuse(n))


def altMaxListe(n_max:int)->list:
    """Retourne la liste de toutes les altitudes maximales de 1 à n-max."""
    return [altMax(i) for i in range(1, n_max+1)]

liste_alt = altMaxListe(10000)
alt_max = max(liste_alt)
print("L'entier", liste_alt.index(alt_max)+1, "a la plus grande altitude maximale égal à", alt_max)