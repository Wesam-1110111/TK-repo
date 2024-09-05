# from tkinter import ttk
import tkinter as tk
import ttkbootstrap as ttk
from user_password import data


def check():
    # print(user.get())
    if user.get() == data[0] and password.get() == data[1]:
        print('COOL!')
        root.quit()

    else:
        print('user name or password is wrong')


# create a window
root = ttk.Window()
w = 1200 / 2
h = 600 / 2
x = root.winfo_screenwidth() / 2 - w
y = root.winfo_screenheight() / 2 - h

# print(x)
# print(y)

root.title('Log in')
root.geometry(f'1200x600+{int(x)}+{int(y)}')
# root.resizable(False, False)

# the body
frame = ttk.Frame(root, borderwidth=2, relief=tk.GROOVE, width=500, height=400)
frame.pack_propagate(False)
frame.pack(pady=50)

# title
title = ttk.Label(frame, text='Log in', font='Calibri 20 bold')
title.pack(pady=25)

# user frame
user_frame = ttk.Frame(frame)
user_frame.pack(pady=10)

# user label
user_label = ttk.Label(user_frame, text='User name: ')
user_label.pack(side='left')

# user name variable
user = tk.StringVar()

# user entry
user_entry = ttk.Entry(user_frame, textvariable=user)
user_entry.pack()

# ----------
# password frame
password_frame = ttk.Frame(frame)
password_frame.pack(pady=10)

# password label
password_label = ttk.Label(password_frame, text='Password: ')
password_label.pack(side='left')

# password name variable
password = tk.StringVar()

# password entry
password_entry = ttk.Entry(password_frame, textvariable=password, show='*')
password_entry.pack()

# submit button
submit_button = ttk.Button(frame, text='Submit', command=check)
submit_button.pack(pady=10)


# make some change
root.bind('<Escape>', lambda event: root.quit())
# root.attributes('-fullscreen', True)
root.attributes('-alpha', 0.95)

# screen
# print(root.winfo_screenwidth())
# print(root.winfo_screenheight())
# print(frame.winfo_x())
# print(user_frame.winfo_y())

# some text
# root.overrideredirect(True)

grip = ttk.Sizegrip(root)
grip.place(relx=1.0, rely=1.0, anchor='se')

# run
root.mainloop()
