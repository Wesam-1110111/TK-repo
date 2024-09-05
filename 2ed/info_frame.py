import tkinter as tk
from tkinter import ttk
import time
import datetime
# import hijri_converter



class Info(ttk.Frame):

	def __init__(self, master):
		super().__init__(master)
		# self.background = bg

		# time
		self.time = datetime.datetime.now()

		# create widgets

		self.create_columns_rows()

		label1 = ttk.Label(self, text=f'Year: {self.time.year}', background='#4747FF', font=("Helvetica", 18))
		label1.grid(row=0, column=0, sticky='nsew')
		
		label2 = ttk.Label(self, text=f'Month: {self.time.strftime('%B')}', background='#4747FF', font=("Helvetica", 18))
		label2.grid(row=1, column=0, sticky='nsew')
		
		label3 = ttk.Label(self, text=f'Day: {self.time.strftime('%A')}', background='#4747FF', font=("Helvetica", 18))
		label3.grid(row=2, column=0, sticky='nsew')
		
		label4 = ttk.Label(self, text=f'Day in the year: {self.time.strftime('%j')}/365', background='#4747FF', font=("Helvetica", 18))
		label4.grid(row=3, column=0, sticky='nsew')

		date = self.time.strftime('%Y') + '/' + self.time.strftime('%m') + '/' + self.time.strftime('%d')

		label5 = ttk.Label(self, text=f'Date: {date}', background='#4747FF', font=("Helvetica", 18))
		label5.grid(row=4, column=0, sticky='nsew')



		self.pack(expand=True, fill='both')


	def create_columns_rows(self):
		self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
		self.columnconfigure((0), weight=1, uniform='a')





if __name__ == '__main__':
	
	# setups
	root = tk.Tk()
	root.geometry('300x300')
	

	Info(root)
	date = datetime(2024, 7, 14)
	hijri_date = convert_Gregorian(date.year, date.month, date.day)

	# run
	root.mainloop()