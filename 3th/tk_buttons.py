import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Tkinter Buttons')
root.minsize(300, 150)

# check box

check_var = tk.BooleanVar()

c = ttk.Checkbutton(
    root,
    text='I\'m 18 or older.',
    variable=check_var,
    onvalue=True,
    offvalue=False
)

c.pack()

# radio buttons

radio_var = tk.StringVar()

r1 = ttk.Radiobutton(
    root,
    text='A. I\'m a Student',
    variable=radio_var,
    value='A'
)

r1.pack()

r2 = ttk.Radiobutton(
    root,
    text='B. I\'m an Employee',
    variable=radio_var,
    value='B'
)

r2.pack()

root.mainloop()
