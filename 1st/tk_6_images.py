from tkinter import *
from PIL import ImageTk, Image
import ttkbootstrap as ttk


index = 0


def back():
    global index
    global label
    global back_btn
    global images
    global state_bar

    front_btn.config(state=ACTIVE)

    if index != 0:

        index -= 1
        if index == 0:
            back_btn.config(state=DISABLED)

    label = Label(image=images[index])
    label.grid(row=0, column=0, columnspan=3)

    # state_bar = Label(root, text=f"Image {index + 1} of {len(images)}", font=12, pady=25)
    state_bar.config(text=f"Image {index + 1} of {len(images)}")
    state_bar.grid(row=2, column=0, columnspan=3)


def front():
    global index
    global label
    global front_btn
    global images
    global state_bar

    back_btn.config(state=ACTIVE)

    if index != len(images) - 1:

        index += 1
        if index == len(images) - 1:
            front_btn.config(state=DISABLED)

    label = Label(image=images[index])
    label.grid(row=0, column=0, columnspan=3)

    # state_bar = Label(root, text=f"Image {index + 1} of {len(images)}", font=12, pady=25, bd=1)
    state_bar.config(text=f"Image {index + 1} of {len(images)}")
    state_bar.grid(row=2, column=0, columnspan=3)


root = ttk.Window(themename='darkly')
root.title("Images")
# root.geometry("500x500")


image1 = ImageTk.PhotoImage(Image.open(f"images/0.jpg"))
image2 = ImageTk.PhotoImage(Image.open(f"images/1.jpg"))
image3 = ImageTk.PhotoImage(Image.open(f"images/2.jpg"))
image4 = ImageTk.PhotoImage(Image.open(f"images/3.jpg"))
image5 = ImageTk.PhotoImage(Image.open(f"images/4.jpg"))

images = [image1, image2, image3, image4, image5]


back_btn = ttk.Button(root, text='<<', command=back, state=DISABLED)
exit_btn = ttk.Button(root, text='Exit', command=root.quit)
front_btn = ttk.Button(root, text='>>', command=front)

state_bar = Label(root, text=f"Image {index + 1} of {len(images)}", font=12, pady=25, padx=80, bd=3, relief=SUNKEN)
state_bar.grid(row=2, column=0, columnspan=3, pady=5)

back_btn.grid(row=1, column=0)
exit_btn.grid(row=1, column=1, pady=15)
front_btn.grid(row=1, column=2)

label = ttk.Label(image=images[index])
label.grid(row=0, column=0, columnspan=3)

root.mainloop()
