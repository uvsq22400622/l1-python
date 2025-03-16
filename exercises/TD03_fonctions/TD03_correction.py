#TD03_correction
def tempsEnSecondes(temps:tuple[int,int,int,int])->int:
    """ Renvoie le total du jour, de l'heure, de la minute et la seconde en secondes."""    
    return temps[0] * 24 * 3600 + temps[1] * 3600 + temps[2] * 60 + temps[3]

temps = ( 3, 23, 1, 34)
print(type(temps))
print(tempsEnSecondes(temps))
#utiliser mypy

def secondesEnTemps(seconde:int)->tuple[int,int,int,int]:
    """Renvoie le total des secondes en jours, en heures, en minutes et en secondes."""
    jour = seconde // 86400
    r = seconde % 86400
    heure = seconde // 3600
    r = r % 3600
    minute = r // 60
    seconde = r % 60
    return (jour,heure,minute,seconde)

temps = 1000000
print(secondesEnTemps(temps))

def affichepluriel(mot:str, nombre:int)-> None:
    if nombre > 0:
        print("", nombre, mot, end="")
    if nombre > 1:
        print("s", end="")

def afficheTemps(temps:tuple[int, int, int, int])-> None:
    affichepluriel("jour", temps[0])
    affichepluriel("heure", temps[1])
    affichepluriel("minute", temps[2])
    affichepluriel("seconde", temps[3])

afficheTemps((1,0,14,23))
#tester aussi avec mypy

def demandeTemps():
    """Demande à l'utilisateur d'entrer un nombre de jours, d'heures, de minutes, et de secondes."""
    