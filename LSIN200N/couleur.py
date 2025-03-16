import tkinter as tk
import random

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    """Colorie le pixel (i,j) de la couleur : color"""
    canvas.create_rectangle(i,j,i+1, j+1, fill=color,width=0)

def ecran_aleatoire():
    """Affiche un canevas avec chaque pixel de couleurs différentes"""
    for i in range(256):
        for j in range(256):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            color = get_color(r,g,b)
            draw_pixel(i ,j ,color)

def degrade_gris():
    """Affiche un dégradé de gris."""
    for i in range(256):
        for j in range(256):
            gris = (i + j) // 2  #=> moyenne pour avoir un dégradé en diagonal
            color = get_color(gris, gris, gris)
            draw_pixel(i, j, color)

def degrade_2D():
    """Affiche un dégradé de rouge à bleu."""
    for i in range(256):
        for j in range(256):
            r = i
            b = 255 - j
            color = get_color(r, 0, b)  # le rouge qui augmente et le bleu qui diminue
            draw_pixel(i, j, color)

racine = tk.Tk()
racine.title("Couleurs")
canvas = tk.Canvas(racine, bg="black", height=256, width=256)
canvas.grid(row=0, column=0, columnspan=3)

bouton_aléatoire = tk.Button(racine, text="Aléatoire", command=ecran_aleatoire)
bouton_aléatoire.grid(row=1, column=1)

bouton_degrade_gris = tk.Button(racine, text="Dégradé gris", command=degrade_gris)
bouton_degrade_gris.grid(row=1, column=2)

bouton_degrade_2D = tk.Button(racine, text="Dégradé 2D", command=degrade_2D)
bouton_degrade_2D.grid(row=1, column=3)

racine.mainloop() 