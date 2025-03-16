import tkinter as tk

def affichage(event):
    canvas.create_line(event.x,event.y,event.x+1,event.y+1, fill="red",width=0)
def dessinee_ligne(event):
    ()
racine = tk.Tk()
racine.title("Clic")

canvas = tk.Canvas(racine, bg="black", height=500, width=500)
canvas.grid(row=0, column=0, columnspan=3)

racine.bind("<Button-1>", affichage)
racine.mainloop()