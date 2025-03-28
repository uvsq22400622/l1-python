import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk 
  
# Définition des variables globales
matrice_pixels_affichee = None
nom_fichier = None
canvas = None
photo = None
matrice_pixels = None

# Gestion de l'affichage
def rafraichir(matrice_pixels):
    global photo, canvas
    
    photo = ImageTk.PhotoImage(Image.fromarray(matrice_pixels))
    
    if canvas is None:
        # Si c'est la première fois qu'on affiche l'image, on crée le canvas
        canvas = tk.Canvas(fenetre_principale, width = (Image.fromarray(matrice_pixels)).size[0], height = (Image.fromarray(matrice_pixels)).size[1])
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.pack()
        create=False
    else:
        # Si le canvas a déjà été créé, on le met simplement à jour avec
        # la nouvelle image à afficher
        canvas.delete("all")
        canvas.config(width=(Image.fromarray(matrice_pixels)).size[0], height=(Image.fromarray(matrice_pixels)).size[1])
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    fenetre_principale.pack_propagate(True)   
    
def ouvrir_dialogue_luminosite():
    global dialogue_effet
    dialogue_effet = tk.Toplevel(fenetre_principale)
    dialogue_effet.title("Luminosité")
    dialogue_effet.geometry("300x150")
    dialogue_effet.grab_set()
    slider = tk.Scale(dialogue_effet, from_=0.1, to=3.0,
                      orient=tk.HORIZONTAL, length=200,
                      resolution=0.1, digits=2,
                      command=correction_gamma)
    slider.set(1.0)
    slider.pack(pady=20)

    frame_boutons = tk.Frame(dialogue_effet)
    frame_boutons.pack(side=tk.BOTTOM, pady=10)

    bouton_appliquer = tk.Button(frame_boutons, text="Appliquer",
                                 command=applique_effet)
    bouton_appliquer.pack(side=tk.LEFT, padx=10)

    bouton_annuler = tk.Button(frame_boutons, text="Annuler",
                               command=annule_effet)
    bouton_annuler.pack(side=tk.LEFT, padx=10)

def correction_gamma(gamma_str):
    global matrice_pixels, matrice_pixels_affichee
    if matrice_pixels is not None:
        gamma = float(gamma_str)
        max_value = float(np.iinfo(matrice_pixels.dtype).max)
        img_normalisee = matrice_pixels / max_value
        img_ajustee = np.power(img_normalisee, gamma)
        matrice_pixels_affichee = (img_ajustee * max_value).astype(matrice_pixels.dtype)
        rafraichir(matrice_pixels_affichee)
#sigmoide utile dans beaucoup de cas 

def ouvrir_dialogue_contraste():
    global dialogue_effet
    dialogue_effet = tk.Toplevel(fenetre_principale)
    dialogue_effet.title("Contraste")
    dialogue_effet.geometry("300x150")
    dialogue_effet.grab_set()

    slider1 = tk.Scale(dialogue_effet, from_=0.0, to=10.0, 
                        orient=tk.HORIZONTAL, length=200,
                        resolution=0.1, digits=2,
                        command=lambda x: correction_sigmoide(slider1.get(), slider2.get()))
    slider1.set(10.0)
    slider1.pack(pady=10)

    slider2 = tk.Scale(dialogue_effet, from_=0.0, to=10.0,
                        orient=tk.HORIZONTAL, length=200,
                        resolution=0.1, digits=2,
                        command=lambda x: correction_sigmoide(slider1.get(), slider2.get()))
    slider2.set(10.0)
    slider2.pack(pady=10)

    frame_boutons = tk.Frame(dialogue_effet)
    frame_boutons.pack(side=tk.BOTTOM, pady=10)

    bouton_appliquer = tk.Button(frame_boutons, text="Appliquer", command=applique_effet)
    bouton_appliquer.pack(side=tk.LEFT, padx=10)

    bouton_annuler = tk.Button(frame_boutons, text="Annuler", command=annule_effet)
    bouton_annuler.pack(side=tk.LEFT, padx=10)

#rajout de label luminosité/contraste et contraste/pente, la modification du slider doit être sur des float:0.000 mais dépend de la linéarisation de la correction gamma

def correction_sigmoide(contraste, pente):
    global matrice_pixels, matrice_pixels_affichee
    if matrice_pixels is not None:
        #normalisation:
        x = np.clip(matrice_pixels, 0, 255) / 255.0
        #transformation sigmoide centrée autour de 0.5
        x = x - 0.5 #centrage
        contraste = float(contraste)
        pente = float(pente)
        #calcul de la fonction
        exposant = (-pente) * contraste * x
        img_ajustee = 1 / (1 + np.exp(exposant))
        #conversion de l'image ajustée entre 0 et 255
        matrice_pixels_affichee = (img_ajustee * 255).astype(np.uint8)
        rafraichir(matrice_pixels_affichee)

#pour trouver les bugs, ajouter des print(les variables qui nous interesse)
#pas version finale de 0 à 10, à faire avec la linéarité

def applique_effet():
    global matrice_pixels, matrice_pixels_affichee, dialogue_effet
    if matrice_pixels_affichee is not None:
        matrice_pixels = matrice_pixels_affichee.copy()
        rafraichir(matrice_pixels)
    if dialogue_effet:
        dialogue_effet.destroy() 

def annule_effet():
    global matrice_pixels, matrice_pixels_affichee, dialogue_effet
    if matrice_pixels is not None:
        matrice_pixels_affichee = matrice_pixels.copy()
        rafraichir(matrice_pixels_affichee)
    if dialogue_effet:
        dialogue_effet.destroy()

def filtre_gris():
    global matrice_pixels
    if matrice_pixels is not None :
        luminance = np.dot(matrice_pixels[:,:,:3].reshape(-1,3),[0.299,0.587,0.114])
        #reshape = pour réorganiser les pixels de l'image(h,l,3) en (h*l,3)
        luminance_reshape = luminance.reshape(matrice_pixels.shape[0],matrice_pixels.shape[1])
        #réorganise pour mettre sous forme hauteur, largeur
        matrice_pixels_gris = np.stack([luminance_reshape]*3, axis=-1)
        #créer la matrice avec les valeurs de l dans les trois canaux / axis=-1 : les canaux soit le dernier axe d'un tableau
        matrice_pixels = np.clip(matrice_pixels_gris, 0, 255).astype(np.uint8)

def filtre_vert():
    global matrice_pixels
    matrice_pixels[:,:,[0,2]] = 0 

# Callbacks
def callback_vert():
    filtre_vert()
    rafraichir(matrice_pixels)

def callback_ouvrir():
    global photo, nom_fichier, matrice_pixels
    nom_fichier = filedialog.askopenfilename(title="Choisir une image", filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if nom_fichier:
        image_pil = Image.open(nom_fichier)
        matrice_pixels = np.array(image_pil)
        rafraichir(matrice_pixels)

def callback_gris():
    filtre_gris()
    rafraichir(matrice_pixels)

def callback_luminosite():
    luminosite()
def callback_correction_gamma():
    correction_gamma()

# Création de la fenêtre principale
fenetre_principale = tk.Tk()
fenetre_principale.title("UVSQolor")

menu_bar = tk.Menu(fenetre_principale)
fenetre_principale.config(menu=menu_bar)

menu_fichier = tk.Menu(menu_bar)
menu_fichier.add_command(
    label="Ouvrir",
    command = callback_ouvrir,
)

menu_effets = tk.Menu(menu_bar)
menu_effets.add_command(
    label="Filtre Vert",
    command=callback_vert,
)

menu_effets.add_command(
    label="Filtre Gris",
    command=callback_gris,
)

menu_bar.add_cascade(
    label="Fichier",
    menu=menu_fichier, 
)

menu_bar.add_cascade(
    label = "Effets",
    menu=menu_effets
)

menu_effets.add_command(
    label="Luminosité", 
    command=ouvrir_dialogue_luminosite
)

menu_effets.add_command(
    label="Contraste",
    command=ouvrir_dialogue_contraste
)

# Boucle principale
fenetre_principale.mainloop()