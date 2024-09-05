import tkinter as tk
from tkinter import ttk

USER = 'admin'
PASSWORD = '1234'


def check():
    if user.get() == USER and password.get() == PASSWORD:
        print('cool')
        frame.forget()
        master_frame.pack()
    else:
        print('user name or password is wrong')


root = tk.Tk()
root.geometry('600x400')
root.attributes('-topmost', True)


# ----------------------------- 1 ------------------------------
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

# --------------------------------------------------------------

# frame 2

# ------------------------------- 2 ----------------------------

master_frame = ttk.Frame(root)
# frame 1
frame1 = ttk.Frame(master_frame, borderwidth=10, relief=tk.GROOVE)
l1 = ttk.Label(frame1, background='#FF8998', text='this is a label in the 1st frame')
l1.pack(expand=True, fill='both')
l2 = ttk.Label(frame1, background='#8989FF', text='another label in the same frame')
l2.pack(expand=True, fill='both')
frame1.pack(ipady=70, ipadx=120)


# just a label
ml = ttk.Label(master_frame, text='The Middel Label', background='#89FF89')
ml.pack(expand=True)


# frame 2
frame2 = ttk.Frame(master_frame, borderwidth=10, relief=tk.GROOVE)

# left frame
left_frame = ttk.Frame(frame2, borderwidth=5, relief=tk.GROOVE)

b1 = ttk.Button(left_frame, text='a button')
b1.pack(side='left', expand=True, fill='y')

l3 = ttk.Label(left_frame, text='a last label', background='#FFFF11')
l3.pack(side='left', expand=True, fill='y')

b2 = ttk.Button(left_frame, text='a button')
b2.pack(side='left', expand=True, fill='y')

left_frame.pack(side='left', expand=True, ipady=70)

# right frame
frame3 = ttk.Frame(frame2)

btn1 = ttk.Button(frame3, text='a button 4')
btn1.pack(side='top', expand=True, fill='both')

btn2 = ttk.Button(frame3, text='a button 5')
btn2.pack(side='top', expand=True, fill='both')

btn3 = ttk.Button(frame3, text='a button 6')
btn3.pack(side='top', expand=True, fill='both')


frame3.pack(side='left', expand=True, ipady=50)

frame2.pack(expand=True)

# --------------------------------------------------------------

# run
root.mainloop()
