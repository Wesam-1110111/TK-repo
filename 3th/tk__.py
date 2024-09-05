# import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def forward():
    home.forget()


def back():
    pass


root = ttk.Window(themename='darkly')
root.title('Test')
root.geometry('800x600')

home = ttk.Frame(root)

title = ttk.Label(home, text="School Management System")

frame = ttk.Frame(home)

b1 = ttk.Button(frame, text='Teachers', command=forward)
# b1.bind('<>', lambda event: print('dfs'))

b2 = ttk.Button(frame, text='Students', command=forward)

home.pack()
title.pack()
frame.pack()
b1.pack()
b2.pack()

teacher = ttk.Frame(root)


root.mainloop()
