from tkinter import *


root = Tk()
num1 = Entry(root)
num1.grid(row=0, column=0)
Label(root,  text="  X  ").grid(row=0, column=1)
num2 = Entry(root)
num2.grid(row=0, column=2)


def click():
    n1 = num1.get()
    n2 = num2.get()
    if n1.isdigit() and n2.isdigit():
        n1 = int(n1)
        n2 = int(n2)
        Label(root, text=n1*n2).grid()
    else:
        num1.insert(0, 1)
        Message(root, text="error", fg="red").grid()


title = "Inputs"
width = "500"
height = "500"


root.geometry(f"{width}x{height}")
root.title(title)

Button(root, text="Click me!", fg="#123456", bg="#7772A0", activebackground="#777777", command=click).grid(row=1, column=1)

root.mainloop()
