#td3 
#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps:tuple)->int:
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps[0]*24*3600 + temps[1]*3600 + temps[2]*60 + temps[3]

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde:int)->tuple[int,int,int,int]:
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jours = seconde // 86400
    r = seconde % 86400
    heure = r // 3600
    r = r% 3600
    minutes = r // 60
    secondes = r % 60
    return (jours, heure, minutes, secondes)
    
temps = 1000000
print(secondeEnTemps(temps))

def afficheTemps(temps:tuple):
