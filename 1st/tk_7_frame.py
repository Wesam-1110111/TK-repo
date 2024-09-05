from tkinter import *
import random

c = [str(i) for i in range(10)]
c += 'A', 'B', 'C', 'D', 'E', 'F'


def random_color():
    color = "#"
    for i in range(6):
        color += random.choice(c)
    print(color)
    frame.config(bg=color)


root = Tk()
root.title("Frames")

frame = LabelFrame(root, text='this label frame', padx=50, pady=50)
frame.pack(padx=15, pady=15)

btn = Button(frame, text='click me', padx=5, pady=5, command=random_color)
btn.pack()


root.mainloop()
