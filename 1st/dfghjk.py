from tkinter import *
# import tkinter as tk

window = Tk()

window.title("First GUI")
window.geometry("500x500")
# window.resizable(False, False)
button = Button(window, text="Print Something", bg="#0FA1B9", fg="#81F0A2", font=80, activebackground="#81F0AF")
lp = Label(window, text="This is a Label", width=150, height=5, font=80, fg="#A112A3")

lp.pack()
button.pack()

# print(button)
print(dir(window))

window.update()
window.mainloop()
