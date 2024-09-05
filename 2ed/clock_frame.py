import tkinter as tk
from tkinter import ttk
# from clock_project import App
import datetime
import time



class Clock(ttk.Frame):

	def __init__(self, master):
		super().__init__(master)
		self.time_format = '12'
		
		# clock widget
		self.colck = tk.Label(self, text='Loading...', bg='black', font=("Helvetica", 48), fg='white')
		self.colck.pack()
		
		# check buttons
		# 12 -> 24 -> 12
		self.time_var = tk.StringVar(value='%p %I:%M:%S')
		check1 = ttk.Checkbutton(self, text='12', variable=self.time_var, onvalue='%p %I:%M:%S', offvalue='%H:%M:%S', command=self.update_time)
		check2 = ttk.Checkbutton(self, text='24', variable=self.time_var, onvalue='%H:%M:%S', offvalue='%p %I:%M:%S', command=self.update_time)
		check1.pack(side='right')
		check2.pack(side='right')


		# update clock
		self.update_time()
		


		# display the widget
		self.pack()
	

	def update_time(self):
		current_time = time.strftime(self.time_var.get())
		self.colck.config(text=current_time)
		self.colck.after(1000, self.update_time)


