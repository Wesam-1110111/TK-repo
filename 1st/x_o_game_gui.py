from tkinter import *
import random


def check_winner():
    for row in range(3):
        if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] != '':
            board[row][0]['bg'] = "green"
            board[row][1]['bg'] = "green"
            board[row][2]['bg'] = "green"

            return True

    for column in range(3):
        if board[0][column]['text'] == board[1][column]['text'] == board[2][column]['text'] != '':
            board[0][column]['bg'] = "green"
            board[1][column]['bg'] = "green"
            board[2][column]['bg'] = "green"

            return True

    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != '':
        board[0][0]['bg'] = "green"
        board[1][1]['bg'] = "green"
        board[2][2]['bg'] = "green"

        return True

    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != '':
        board[0][2]['bg'] = "green"
        board[1][1]['bg'] = "green"
        board[2][0]['bg'] = "green"

        return True


def check_tie():
    space = 9
    if not check_winner():
        for row in range(3):
            for column in range(3):
                if board[row][column]['text'] != '':
                    space -= 1
        if space == 0:
            label.config(text='Tie!')
        return space == 0
    return False



def reset_game():

    global player

    for row in range(3):
        for column in range(3):
            board[row][column]['text'] = ''

    player = random.choice(players)
    label.config(text=player + ' turn')
    for row in range(3):
        for column in range(3):
            board[row][column]['bg'] = '#F0F0F0'


def next_turn(row, column):

    global player

    if board[row][column]["text"] == "" and not check_winner():
        # board[row][column]['text'] = player
        
        if player == players[0]:
            board[row][column]['text'] = player

            if not check_winner():
                player = players[1]
                label.config(text=player + ' turn')
        else:
            board[row][column]['text'] = player

            if not check_winner():
                player = players[0]
                label.config(text=player + ' turn')
    check_tie()



window = Tk()

window.iconbitmap('C:\\Users\\TOSHIBA\\Downloads\\tic-tac-toe_39453.ico')
window.title("Tic Tac Toe")
# window.geometry("500x500")
players = ['x', 'o']
player = random.choice(players)

label = Label(text=player + " turn", font=("consolas", 40))
label.pack(side='top')

reset_btn = Button(window, text='restart', font=('consolas', 20), command=reset_game)
reset_btn.pack(side='top')

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        board[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                    command= lambda row=row, column=column: next_turn(row, column))
        board[row][column].grid(row=row, column=column)


window.mainloop()
