# from tkinter import *
# import tkinter as tk
# from tkinter import ttk
# import ttkbootstrap as ttk
from ttkbootstrap import *


def convert():
    if text_box.get().isdigit():
        output.config(text=int(text_box.get()) * 1.609)


root = Window()
root.title("Converter")
root.geometry("300x150")

title = Label(root, text="Miles to kilometers", font='Calibri 24 bold')
title.pack()

frame = Frame(root)
frame.pack(pady=10)

text_box = Entry(frame, font='Calibri')
text_box.pack(side='left', padx=15)

btn = Button(frame, text='Convert', command=convert)
btn.pack(side='left')

output = Label(root, text=0, font='Calibri 24')
output.pack(pady=5)

root.mainloop()
