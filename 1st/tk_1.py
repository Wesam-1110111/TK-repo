from tkinter import *

root = Tk()
root.geometry("500x500")
myl = Label(root, text="zii")
myl2 = Label(root, text="Hello from the top")

Button(root, text="Click to flick").grid(row=0, column=3)

# myl.pack()
myl.grid(row=0, column=0)
myl2.grid(row=5, column=10)

root.mainloop()
