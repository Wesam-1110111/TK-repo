from main import root
from tkinter import ttk
import tkinter as tk


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
submit_button = ttk.Button(frame, text='Submit')
submit_button.pack(pady=10)
