# # # importing only those functions which
# # # are needed
# # from tkinter import Tk, mainloop, TOP
# # from tkinter.ttk import Button

# # # time function used to calculate time
# # from time import time

# # # creating tkinter window
# # root = Tk()

# # button = Button(root, text = 'Geeks')
# # button.pack(side = TOP, pady = 5)

# # print('Running...')
# # # Calculating starting time
# # start = time()

# # # in after method 5000 milliseconds
# # # is passed i.e after 5 seconds
# # # main window i.e root window will
# # # get destroyed
# # root.after(5000, root.destroy)

# # mainloop()

# # # calculating end time
# # end = time()
# # print('Destroyed after % d seconds' % (end-start))

# # importing only those functions which
# # are needed
# from tkinter import Tk, mainloop, TOP
# from tkinter.ttk import Button
# from tkinter.messagebox import _show

# # creating tkinter window
# root = Tk()
# root.geometry('200x100+300+250')

# button = Button(root, text = 'Geeks')
# button.pack(side = TOP, pady = 5)

# # in after method 5000 milliseconds
# # is passed i.e after 5 seconds
# # a message will be prompted
# root.after(3000, lambda : _show('Title', 'Prompting after 5 seconds'))

# # Destroying root window after 6.7 seconds
# root.after(9700, root.destroy)

# mainloop()


import tkinter as tk
from tkinter import Label, messagebox
import time

time_format = '12'


def alert(time):
    if time == '58':
        messagebox.showinfo("Time Alert", "Hi.")



def time_update():
    if time_format == '12':
        current_time = time.strftime("%p %I:%M:%S")
    else:
        current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    # print(type(time.strftime('%M')))
    alert(time.strftime('%M'))
    clock_label.after(1000, time_update)

# 
root = tk.Tk()
root.title("Digital Clock")
root.overrideredirect(True)
root.attributes('-topmost', True)
# 
clock_label = Label(root, font=("Helvetica", 28), bg="black", fg="white")
clock_label.pack(anchor='center')
root.bind('<c>', lambda event: root.quit())
# 
time_update()

# 
root.mainloop()
