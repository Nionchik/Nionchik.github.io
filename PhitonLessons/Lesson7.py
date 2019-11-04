from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=400, height=500)
canvas.pack()



def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(x1 + random.randrange(width))
    y2 = random.randrange(y1 + random.randrange(height))
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)

random_rectangle(400, 400, "green")
random_rectangle(200, 350, "red")
random_rectangle(450, 450, "green")
random_rectangle(400, 400, "blue")
random_rectangle(400, 400, "black")
random_rectangle(400, 400, "#ffd800")
random_rectangle(400, 400, "#ffd800")

