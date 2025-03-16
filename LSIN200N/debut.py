import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

root = tk.Tk() #modif

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT) #modif

    # Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100
y = CANVAS_HEIGHT / 2
canvas.create_line((CANVAS_WIDTH/2), 100, (CANVAS_WIDTH/2), (CANVAS_HEIGHT-100)) #modif
canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)
canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
    
    # Fin de votre code

canvas.grid()
root.mainloop()