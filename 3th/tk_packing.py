import tkinter as tk
from tkinter import ttk


# create a window
root = tk.Tk()
root.title('Packing and Frames')
root.geometry('400x600+900+50')
root.attributes('-topmost', True)

# the code

# frame 1
frame1 = ttk.Frame(root, borderwidth=10, relief=tk.GROOVE)
l1 = ttk.Label(frame1, background='#FF8998', text='this is a label in the 1st frame')
l1.pack(expand=True, fill='both')
l2 = ttk.Label(frame1, background='#8989FF', text='another label in the same frame')
l2.pack(expand=True, fill='both')
frame1.pack(ipady=70, ipadx=120)


# just a label
ml = ttk.Label(root, text='The Middel Label', background='#89FF89')
ml.pack(expand=True)


# frame 2
frame2 = ttk.Frame(root, borderwidth=10, relief=tk.GROOVE)

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


# run
root.mainloop()
