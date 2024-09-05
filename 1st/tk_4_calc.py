from tkinter import *
from colors import Colors


root = Tk()
root.title("Simple Calculater")
root.resizable(False, False)
box = Entry(root, width=15, borderwidth=1, font='Arial 30')
box.grid(row=0, column=0, columnspan=4, pady=30)

nums = ""


def button_click(number):
    if box.get():
        box.insert(50000, number)
        # Message(root, text="error", fg="#ff0000")
    else:
        box.insert(0, number)


def button_clear():
    box.delete(0, END)


def button_add():
    if box.get():
        global first_number
        global opp
        opp = '+'
        try:
            first_number = int(box.get())
            button_clear()
        except ValueError:
            print(f"{Colors.yellow}Are you insain!{Colors.end}")

def button_equal():
        try:
            sec_number = int(box.get())
            button_clear()
            if opp == '+':
                ans = first_number + sec_number
                box.insert(0, str(ans))

            elif opp == '-':
                ans = first_number - sec_number
                box.insert(0, str(ans))

            elif opp == '*':
                ans = first_number * sec_number
                box.insert(0, str(ans))

            elif opp == '/':
                if sec_number != 0:
                    ans = first_number / sec_number
                    box.insert(0, str(ans))
                else:
                    box.insert(0, "error")
        except ValueError:
            print(f"{Colors.yellow}Sorry, you are stupid{Colors.end}")


b1 = Button(root, text='1', width=15, height=5, command=lambda: button_click(1))
b1.grid(row=3, column=0)

b2 = Button(root, text='2', width=15, height=5, command=lambda: button_click(2))
b2.grid(row=3, column=1)

b3 = Button(root, text='3', width=15, height=5, command=lambda: button_click(3))
b3.grid(row=3, column=2)

b4 = Button(root, text='4', width=15, height=5, command=lambda: button_click(4))
b4.grid(row=2, column=0)

b5 = Button(root, text='5', width=15, height=5, command=lambda: button_click(5))
b5.grid(row=2, column=1)

b6 = Button(root, text='6', width=15, height=5, command=lambda: button_click(6))
b6.grid(row=2, column=2)

b7 = Button(root, text='7', width=15, height=5, command=lambda: button_click(7))
b7.grid(row=1, column=0)

b8 = Button(root, text='8', width=15, height=5, command=lambda: button_click(8))
b8.grid(row=1, column=1)

b9 = Button(root, text='9', width=15, height=5, command=lambda: button_click(9))
b9.grid(row=1, column=2)

b0 = Button(root, text='0', width=15, height=5, command=lambda: button_click(0))
b0.grid(row=4, column=0)

b_clear = Button(root, text='AC', padx=102, pady=30, command=lambda: button_clear(), bg="#FFa64d")
b_clear.grid(row=4, column=1, columnspan=2)

b_add = Button(root, text='+', padx=50, pady=72, command=lambda: button_add())
b_add.grid(row=4, column=3, rowspan=5)

b_sum = Button(root, text='=  ', padx=160, pady=30, command=lambda: button_equal(), bg="#80bfff")
b_sum.grid(row=5, column=0, columnspan=3)


def button_sub():
    if box.get():
        global first_number
        global opp
        opp = '-'
        try:
            first_number = int(box.get())
            button_clear()
        except ValueError:
            print(f"{Colors.yellow}Are you insain!{Colors.end}")


b_sub = Button(root, text='-', width=15, height=5, command=lambda: button_sub())
b_sub.grid(row=3, column=3)


def button_mul():
    if box.get():
        global first_number
        global opp
        opp = '*'
        try:
            first_number = int(box.get())
            button_clear()
        except ValueError:
            print(f"{Colors.yellow}Are you insain!{Colors.end}")


b_mul = Button(root, text='x', width=15, height=5, command=lambda: button_mul())
b_mul.grid(row=2, column=3)


def button_div():
    if box.get():
        global first_number
        global opp
        opp = '/'
        try:
            first_number = int(box.get())
            button_clear()
        except ValueError:
            print(f"{Colors.yellow}Are you insain!{Colors.end}")


b_div = Button(root, text='/', width=15, height=5, command=lambda: button_div())
b_div.grid(row=1, column=3)

root.mainloop()
