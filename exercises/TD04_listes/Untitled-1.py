def syracuse(n:int)->list:
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    r=[n]
    while n!=1:
        if n%2==0:
            n=n/2
            r.append(n)
        else:
            n*=3
            n+=1
            r.append(n)
    return r
print(syracuse(3))

def testeConjecture(n_max:int)-> bool:
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    for i in range(1, n_max):
        syracuse(i)
    return True

print(testeConjecture(10000))

def tempsVol(n:int)->int:
    """ Retourne le temps de vol de n """
    return len(syracuse(n))-1
print("Le temps de vol de", 3, "est", tempsVol(3))

def tempsVolListe(n_max:int)->list:
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    return [tempsVol(i) for i in (1, n_max)]
print(tempsVolListe(100))