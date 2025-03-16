import tkinter as tk
racine = tk.Tk()
racine.title("Titre") 

canvas = tk.Canvas(racine, bg="black")
canvas.grid()

couleur_actuelle = "blue"

canvas.create_text(
    150, # coordonnée x du centre du texte
    20, # coordonnée y du centre du texte
    text="Titre",
    fill="white",  # Couleur du texte
    font=("helvetica", "20"))

def affichage_cercle():
    canvas = tk.Canvas(racine, bg="black", height=500, width=500)
    canvas.grid(row=3, column=0)
    canvas.create_oval((100, 100), (300, 300), fill="blue", width=5, outline="blue")
    return

def affichage_carre():
    canvas = tk.Canvas(racine, bg= "black", height=500, width=500)
    canvas.grid(row=3, column=1)
    canvas.create_rectangle(50, 50, 150, 150, fill="red")
    return

def affichage_croix():
    canvas = tk.Canvas(racine, bg="black", height=500, width=500)
    canvas.grid(row=4, column=0)
    canvas.create_line(50, 50, 150, 150, fill="yellow", width=5)
    canvas.create_line(150, 50, 50, 150, fill="yellow", width=5)

def choisir_couleur():
    global couleur_actuelle
    nouvelle_couleur = input("Entrez une couleur (ex: red, green, blue) : ")
    couleur_actuelle = nouvelle_couleur


bouton_cercle = tk.Button(racine, bg="black", fg="blue",text="cercle", command=affichage_cercle,
                   font = ("helvetica", "20"))
bouton_cercle.grid(row=1, column=0)

bouton_carre = tk.Button(racine, bg="black", fg="red", text="carré", command=affichage_carre,
                   font = ("helvetica", "30"))
bouton_carre.grid(row=2, column=0)

bouton_croix = tk.Button(racine, bg="black", fg="yellow",text="croix", command=affichage_croix, 
                   font = ("helvetica", "10"))
bouton_croix.grid(row=1, column=2)

bouton_couleur = tk.Button(racine, bg="black", fg="orange",text="Choisir une couleur", command=choisir_couleur,
                   font = ("helvetica", "30"))
bouton_couleur.grid(row=2, column=2, columnspan=2)
    
racine.mainloop() #lancement de la boucle

#pas fini