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
#print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

def afficheTemps(temps):
    """ Affiche un message exprimant le temps"""
    if temps[0] > 1:
        print("Il y a ", temps[0], " jours, ", end="")
    elif temps[0] == 1:
        print("Il y a ", temps[0], " jour, ", end="")
    elif temps[0] == 0:
        print("Il y a ",end="")
    if temps[1] > 1:
        print(temps[1], "heures, ", end="")
    elif temps[1] == 0:
        print(end="")
    if temps[2] > 1:
        print(temps[2], "minutes et ", end="")
    elif temps[2] == 0:
        print(end="")
    if temps[3] > 1:
        print(temps[3], "secondes !")
    elif temps[3] == 0:
        print("!",end="")              
    
afficheTemps((1,0,14,23))

def demandeTemps():
    """Demande à l'utilisateur d'entrer un nombre de jours, d'heures, de minutes, et de secondes."""
    jours = int(input("jours"))
    heures = int(input("heures"))
    minutes = int(input("minutes"))
    secondes = int(input("secondes"))
    duree = [jours, heures, minutes, secondes]
    for i in duree :
        if heures > 24:
            heures = int(input("Entrer une valeur entre 0 et 23 !"))
        else:
            continue
        if minutes > 60:
            minutes = int(input("Entrer une valeur entre 0 et 59 !"))
        else:
            continue
        if secondes > 60:
            secondes = int(input("Entrer une valeur entre 0 et 59 !"))
    durée = [jours, heures, minutes, secondes]
    return duree

afficheTemps(demandeTemps())

def sommeTemps(temps1,temps2):
    """Effectue la somme de deux temps donnés."""
    somme = (temps1[0] + temps2[0],temps2[1]+temps2[1],temps1[2]+temps2[2],temps1[3]+temps2[3])
    afficheTemps(somme)

sommeTemps((2,3,4,25),(5,22,57,1))

def proportionTemps(temps, proportion):
    """Donne la proportion d'un temps."""
    temps = (temps[0] // proportion, temps[1] // proportion, temps[2] // proportion, temps[3] // proportion)
    return temps
afficheTemps(proportionTemps((2,0,36,0),0.2))

def tempsEnDate(temps):
    """Donne la date sous la forme (année, jour, heure, minute, seconde), retourne un tuple (année, mois, jour, heure, minute, seconde)"""
    annee = 1970
    jour_annee = 0
    jour_par_annee = 365
    
    #année
    while temps >= jour_par_annee * 60 * 60 * 24:
        annee += 1
        temps -= jour_par_annee * 60 * 60 * 24
        if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
            jour_par_annee = 366
        else:
            jour_par_annee = 365
    #jour
    jour_par_annee = temps // (60 * 60 * 24 )
    #heures,minutes,secondes
    reste = temps % (60 * 60 * 24)
    heure = reste // (60 * 60)
    reste %= (60 * 60)
    minute = reste // 60
    seconde = reste % 60
    mois = jour_annee // 30 + 1
    date = (annee, mois, jour_annee + 1, heure, minute, seconde)
    return date


def afficheDate(date = -1):
    print(tempsEnDate())
    
temps = secondesEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()

import time
time.gmtime(0)

def bisextile(jour):
    """Affiche toutes les années bisextile depuis le 1er janvier 1970 jusqu'à un nombre donnée de jours."""
    jour = int(input("nombre de jour"))
    jour_par_annee = 365
    secondes_par_jour = 24 * 60 * 60
    temps = 0
    annee = 1970
    while temps <= jour * secondes_par_jour:
        if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
            print(annee)
        annee += 1
        temps += jour_par_annee * 60   
        if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
            jour_par_annee = 366
        else:
            jour_par_annee = 365
    return 
        
bisextile(20000)

def nombreBisextile(jour):
    """Calcule le nombre d'années bisextiles pour un nombre de jour donnés.
        Arg : nombre de jour donnée """
    jour = int(input("nombre de jour"))
    jour_par_annee = 365
    secondes_par_jour = 24 * 60 * 60
    temps = 0
    annee = 1970
    nb_année = 0
    while temps <= jour * secondes_par_jour:
        if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
            print(annee)
        annee += 1
        temps += jour_par_annee * 60   
        if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
            jour_par_annee = 366
            nb_année +=1
        else:
            jour_par_annee = 365
    return nb_année

def tempsEnDateBisextile(temps):
    pass
   
temps = secondesEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))