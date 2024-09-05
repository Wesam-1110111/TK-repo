import tkinter as tk
from tkinter import ttk

# setups
root = tk.Tk()
root.title('Combined layout')
root.geometry('600x600+700+50')
root.minsize(600, 600)
root.attributes('-topmost', True)

# ****-*-**-*-*-*-*-*-*-*-****


class MainFrame:
    pass


# ------- main frames --------

# ***** left frame *****
left_frame = ttk.Frame(root)
left_frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)

# widgets
button1 = ttk.Button(left_frame, text='Button 1')
button2 = ttk.Button(left_frame, text='Button 2')
button3 = ttk.Button(left_frame, text='Button 3')

slider1 = ttk.Scale(left_frame, orient='vertical', from_=0, to=50)
slider2 = ttk.Scale(left_frame, orient='vertical', from_=0, to=50)

# inner frame
inner_frame = ttk.Frame(left_frame)

checkbox_var = tk.StringVar()

check1 = ttk.Checkbutton(inner_frame, text='Yes', onvalue='ON', offvalue='OFF', variable=checkbox_var)
check2 = ttk.Checkbutton(inner_frame, text='No', onvalue='OFF', offvalue='ON', variable=checkbox_var)

entry1 = ttk.Entry(left_frame)

# layout with grid
left_frame.columnconfigure(0, weight=1, uniform='a')
left_frame.columnconfigure(1, weight=1, uniform='a')
left_frame.columnconfigure(2, weight=1, uniform='a')

left_frame.rowconfigure(0, weight=1, uniform='a')
left_frame.rowconfigure(1, weight=1, uniform='a')
left_frame.rowconfigure(2, weight=1, uniform='a')
left_frame.rowconfigure(3, weight=1, uniform='a')
left_frame.rowconfigure(4, weight=1, uniform='a')

button1.grid(row=0, column=0, columnspan=2, sticky='nsew')
button2.grid(row=0, column=2, sticky='nsew')
button3.grid(row=1, column=0, columnspan=3, sticky='nsew')

slider1.grid(row=2, column=0, rowspan=2, sticky='nsew', pady=20)
slider2.grid(row=2, column=2, rowspan=2, sticky='nsew', pady=20)

""" layout inside the inner frame """

inner_frame.grid(row=4, column=0, columnspan=3, sticky='ew')
check1.pack(side='left', expand=True)
check2.pack(side='left', expand=True)
entry1.place(relx=0.5, rely=0.95, relwidth=0.9, anchor='center')

# ***** main frame *****
main_frame = ttk.Frame(root)
main_frame.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)

# ** subs frames **
right_sub_frame = ttk.Frame(main_frame)
left_sub_frame = ttk.Frame(main_frame)

label1 = ttk.Label(right_sub_frame, text='Label 1', background='#FF7878')
label2 = ttk.Label(left_sub_frame, text='Label 2', background='#7878FF')

btn1 = ttk.Button(left_sub_frame, text='Button 1')
btn2 = ttk.Button(right_sub_frame, text='Button 2')

"""  main frame layout  """

right_sub_frame.pack(side='right', expand=True, fill='both', padx=20, pady=20)
left_sub_frame.pack(side='left', expand=True, fill='both', padx=20, pady=20)

label1.pack(expand=True, fill='both')
label2.pack(expand=True, fill='both')

btn1.pack(expand=True, fill='both', pady=10)
btn2.pack(expand=True, fill='both', pady=10)

#

# run
root.mainloop()
