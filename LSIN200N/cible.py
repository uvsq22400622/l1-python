import tkinter as tk
import random as rd

racine = tk.Tk()
racine.title("Cible aléatoire")
CANVAS_SIZE=600
mon_canevas=tk.Canvas(racine, width=CANVAS_SIZE, height=CANVAS_SIZE, bg="black")
mon_canevas.grid()

nb_cercles=30
couleurs=["blue","green","black","yellow","magenta", "red"]

epaisseur=(CANVAS_SIZE//2)//nb_cercles

for i in range(nb_cercles):
    mon_canevas.create_oval(i*epaisseur, i*epaisseur, 
                            CANVAS_SIZE - i * epaisseur, 
                            CANVAS_SIZE - i*epaisseur, 
                            fill=couleurs[i% len(couleurs)],width=0)


racine.mainloop()