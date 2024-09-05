# import datetime
import tkinter as tk
# from tkinter import ttk
# from clock_frame import Clock
import clock_frame
import info_frame


class App(tk.Tk):

	def __init__(self, title: str = 'Clock', size: (int, int) = (300, 300)):
		
		# window setups
		super().__init__()
		self.title(title)
		self.geometry(f'{size[0]}x{size[1]}')
		self.minsize(size[0], size[1])
		# self.overrideredirect(True)
		
		# create frames
		clock_frame.Clock(self)

		info_frame.Info(self)

		# type 'c' to exit
		self.bind('<c>', lambda event: self.quit())

		# run	
		self.mainloop()


if __name__ == '__main__':
	App(title='Clock App', size=(370, 300))
	# root.bind('<c>', lambda event: root.quit())
