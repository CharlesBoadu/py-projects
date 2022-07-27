from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

def callback(r, c):
    global player

    if player == 'X' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='X', bg='white', fg='blue')
        states[r][c] = 'X'
        player = 'O'

    if player == 'O' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='O', bg='black', fg='orange')
        states[r][c] = 'O'
        player = 'X'

    check_for_winner()

def check_for_winner():
    global stop_game

    for i in range(3):
        if states[i][0]==states[i][1]==states[i][2] != 0:
            b[i][0].configure(bg='grey')
            b[i][1].configure(bg='grey')
            b[i][2].configure(bg='grey')
            stop_game = True

    for i in range(3):
        if states[0][i]==states[1][i]==states[2][i] != 0:
            b[0][i].configure(bg='grey')
            b[1][i].configure(bg='grey')
            b[2][i].configure(bg='grey')
            stop_game = True

    if states[0][0]==states[1][1]==states[2][2] != 0:
            b[0][0].configure(bg='grey')
            b[1][1].configure(bg='grey')
            b[2][2].configure(bg='grey')
            stop_game = True

    if states[2][0]==states[1][1]==states[0][2] != 0:
            b[2][0].configure(bg='grey')
            b[1][1].configure(bg='grey')
            b[0][2].configure(bg='grey')
            stop_game = True

def quit_game():
    answer = askquestion(title='Quit Game', message='Do you really want to quit the game?')
    if answer == 'yes':
        root.destroy()

def open_callback():
    filename = askopenfilename()
    
root = Tk()
root.protocol('WM_DELETE_WINDOW', quit_game)
menu = Menu()
root.config(menu=menu)
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='Open Game', command=open_callback)
file_menu.add_command(label='Exit', command=root.destroy)
menu.add_cascade(label='File', menu=file_menu)

states = [[0,0,0],
          [0,0,0],
          [0,0,0]]

b = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('verdana', 56), width=3, bg='yellow', command = lambda  r=i,c=j: callback(r, c))
        b[i][j].grid(row=i, column=j)


player = 'X'
stop_game = False

mainloop()        
