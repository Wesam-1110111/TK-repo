import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window title
root.title("Hello Tkinter")

# Set window size
root.geometry('400x300')

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Run the application
root.mainloop()
