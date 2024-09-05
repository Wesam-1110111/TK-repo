from tkinter import *
from PIL import ImageTk, Image


root = Tk()

root.title("test")
root.geometry("500x500")

exit_btn = Button(root, text='Exit', padx=50, pady=10, command=root.quit)
exit_btn.pack(side='bottom')

img = ImageTk.PhotoImage(Image.open('Untitled.png'))
label = Label(image=img)
label.pack()

root.mainloop()
