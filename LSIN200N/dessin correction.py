import tkinter as tk
import random as rd

racine = tk.Tk() #commande
racine.title("Mon dessin") 

def dessine_disque()->None:
    """ Dessine un disque de rayon 50 pixels sur une position aléatoire du canveas qu est stocké dans la variable globale mon_canevas."""
    centre_x=rd.randint(50, CANVAS_WIDTH - 50)
    centre_y=rd.randint(50, CANVAS_HEIGHT-50)
    mon_canevas.create_oval(centre_x - 50, centre_y - 50, centre_x +50, centre_y +50, fill = couleur)

def dessine_carre()->None:
    """ Dessine un carree de rayon 50 pixels sur une position aléatoire du canveas qu est stocké dans la variable globale mon_canevas."""
    centre_x=rd.randint(50, CANVAS_WIDTH - 50)
    centre_y=rd.randint(50, CANVAS_HEIGHT-50)
    mon_canevas.create_rectangle(centre_x - 50, centre_y - 50, centre_x +50, centre_y +50, fill = couleur)

def dessine_croix()->None:
    """ Dessine une croix de rayon 50 pixels sur une position aléatoire du canveas qu est stocké dans la variable globale mon_canevas."""
    centre_x=rd.randint(50, CANVAS_WIDTH - 50)
    centre_y=rd.randint(50, CANVAS_HEIGHT-50)
    mon_canevas.line(centre_x, centre_y - 50, centre_x, centre_y +50, fill = couleur)
    mon_canevas.line(centre_x - 50, centre_y, centre_x +50, centre_y, fill = couleur)

def change_couleur()->None:
    global couleur 
    couleur=input("Donner une couleur\n")
    
couleur = "blue"

bouton_cercle = tk.Button(racine, text="Cercle", command=dessine_disque)
bouton_couleur = tk.Button(racine, text="Choisir une couleur", commmand=change_couleur)
bouton_carre = tk.Button(racine, text="Carré", command=dessine_carre)
bouton_croix = tk.Button(racine, text="Croix", command=dessine_croix)

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 500

mon_canevas = tk.Canvas(racine, background="Black", widht= CANVAS_WIDTH, height=CANVAS_HEIGHT)

bouton_couleur.grid(row=0, column=1)
bouton_cercle.grid(row=1, column=0)
bouton_carre.grid(row=2, column=0)
bouton_croix.grid(row=3, column=0)

mon_canevas.grid(row=1, column=1, rowspan=3)

racine.mainloop()
