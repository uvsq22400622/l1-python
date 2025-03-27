import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk 
  
nom_fichier = None
canvas = None
photo = None
matrice_pixels = None

def ouvrir():
    global nom_fichier, photo
    nom_fichier = filedialog.askopenfilename(title="Ouvrir une image")
    if nom_fichier is not None:
        # On crée une image Pillow puis on la convertit au format TkInter 
        img = pil.Image.open(nom_fichier)
        photo = ImageTk.PhotoImage(img)

def rafraichir(matrice_pixels):
    global photo
    
    photo = Image.Tk.PhotoImage(Image.fromarray(matrice_pixels))

    canvas.delete("all")
    canvas.config(width=photo.size[0], height=photo.size[1]) #définir la taille
    canvas.create_(0, 0, anchor=tk.NW, image=photo)

    fenetre_principale.pack_propagate(True)

# Gestion de l'affichage
def charger_image():
    global imag, image_affichee
    chemin_fichier = filedialog.askopenfilename()
    if chemin_fichier:
        image_pil = Image.open(chemin_fichier)
        img = np.array(img_pil)
        img_affichee = img.copy() 
        afficher_image(img_affichee)

def affichage_image(matrice):
    global photo, canvas
    if matrice is not None:
        image_pixels = Image.fromarray(matrice)
        photo = ImageTk.PhotoImage(image_pil)
        canvas.config(widht=photo_tk.width(), height=photo_tk.height())
        canvas.create_image(0,0,anchor=tk.NW, image=photo)
    else:
        canvas.delete("all")
        canvas.config(widht=1, height=1)

def ouvrir_dialogue_luminosite():
    global dialogue_effet
    dialogue_effet = tK.Toplevel(fenetre_principale)
    dialogue_effet.title("Luminosité")
    dialogue_effet.geometry("300x150")
    dialogue_effet.grab_set()
    slider = tk.Scale(dialogue_effet, from_=0.1, to=3.0, orient = tk.HORIZONTAL,
            length = 200, resolution = 0.1, digits = 2, command=correction_gamma)
    slider.set(1,0)
    slider.pack(pady=20)
    
    frame_boutons = tk.Frame(dialogue_effet)
    frame_boutons.pack(side=tk.BOTTOM, pady=10)
    
    bouton_appliquer = tk.Button(frame_boutons, text="Appliquer", command=applique_effet)
    bouton_appliquer.pack(side=tk.LEFT, padx=10)
    bouton_annuler = tk.Button(frame_boutons, text="Annuler", command=annule_effet)
    bouton_annuler.pack(side=tk.LEFT, padx=10)


def correction_gamma(gamma_str):
    global img, img_affichee
    if img is not None:
        gamma = float(gamma_str)
        max_value = float(np.iinfo(image.dtype).max)
        img_normalisee = img / max_value
        img_corrigee = np.power(img_normalisee, gamma)
        img_affichee = (img_corrigee * max_value).astype(img.dtype)
        afficher_image(img_affichee)

def applique_effet():
    global img, img_affichee, dialogue_effet
    if img_affichee is not None:
        img_originale = img_affichee.copy()
        afficher_image(img_affichee)
    if dialogue_effet:
        dialogue_effet.destroy() 

def annule_effet():
    global img, img_affichee, dialogue_effet
    if img is not None:
        img_affichee = img.copy()
        afficher_image(img_affichee)
    if dialogue_effet:
        dialogue_effet.destroy()


# Algorithmes de filtre
def filtre_vert():
    global matrice_pixels
    matrice_pixels[:,:,[0,2]] = 0 

def filtre_gris():
    global matrice_pixels
    if matrice_pixels is not None :
        luminance = np.dot(matrice_pixels[:,:,:3],[0.299,0.587,0.114])
        matrice_pixels_gris = np.stack([luminance,luminance,luminance], axis=-1)
        matrice_pixels = matrice_pixels_gris


# Callbacks
def callback_vert():
    filtre_vert()
    rafraichir()

def callback_ouvrir():
    global photo
    photo = ImageTk.PhotoImage(pil.Image.open(nom_fichier))
    rafraichir()

def call_back_gris():
    filtre_gris()
    rafraichir()

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
    command =callback,
)

menu_effets = tk.Menu(menu_bar)
menu_effets.add_command(
    label="Filtre Vert",
    command=callback,
)

menu_effets.add_command(
    label="Filtre Gris",
    command=callback
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

menubar.add_cascade(
    label="Effets", 
    menu=menu_effets
)

# Boucle principale
fenetre_principale.mainloop()
