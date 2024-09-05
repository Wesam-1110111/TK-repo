from tkinter import *


def check_g():
    global frame
    global r
    global r2

    if g.get() == 1:
        frame.config(bg='#5555ff')
        r.config(bg='#5555ff')
        r2.config(bg='#5555ff')

    elif g.get() == 2:
        frame.config(bg='pink')
        r.config(bg='pink')
        r2.config(bg='pink')


root = Tk()
root.title("Radio Button")

frame = LabelFrame(root, text='Options:', font=('consolas', 20), pady=25, padx=25)
frame.pack(pady=15, padx=15)

g = IntVar()

r = Radiobutton(frame, text='Male', variable=g, value=1, font=('consolas', 10))
r2 = Radiobutton(frame, text='Female', variable=g, value=2, font=('consolas', 10))

btn = Button(root, text='check G', command=check_g)
btn.pack(pady=15)

r.pack()
r2.pack()

root.mainloop()
