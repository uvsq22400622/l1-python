import tkinter as tk
import random

def dessiner_cible():
    """Dessine des cercles aléatoires sur le canvas."""
    canvas.delete("all")  # Efface les cercles précédents
    nombre_cercles = int(input("Nombre de cercles : "))
    couleurs = ["blue", "green", "black", "yellow", "magenta", "red"]
    largeur_canvas = canvas.winfo_width()  # Obtient la largeur du canvas
    hauteur_canvas = canvas.winfo_height()  # Obtient la hauteur du canvas

    for _ in range(nombre_cercles):
        rayon = random.randint(10, 50)
        x = random.randint(rayon, largeur_canvas - rayon)
        y = random.randint(rayon, hauteur_canvas - rayon)
        couleur = random.choice(couleurs)
        canvas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, fill=couleur)

# Configuration de la fenêtre principale
racine = tk.Tk()
racine.title("Cible aléatoire")

# Configuration du canvas
canvas = tk.Canvas(racine, width=400, height=400, bg="white")
canvas.grid(column=0, row=0)  # Place le canvas en haut

# Configuration du bouton
bouton = tk.Button(
    text="Créer la cible", command=dessiner_cible, font=("Helvetica", "30")
)
bouton.grid(column=0, row=1)  # Place le bouton en dessous du canvas

racine.mainloop()