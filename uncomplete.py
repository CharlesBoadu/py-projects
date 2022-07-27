from random import randint
from tkinter import *


def math_game():
    global count
    global i
    i += 1
    button.configure(text='Next Question')
    entry.configure(width=4)
    answer_button.configure(text='Answer')
    x = randint(1, 12)
    y = randint(1, 12)
    z = x * y
    label.configure(text='Question {}: {} X {}'.format(i, x, y))
    answer = entry.get()
    if answer == z:
        output_label.configure(text='Right!')
        count += 1
        entry.delete(0, END)
    else:
        output_label.configure(text='Wrong! answer = {}'.format(z))
        entry.delete(0, END)

def answer():
    answer = entry.get()
    if answer == z:
        output_label.configure(text='Right!')
        count += 1
        entry.delete(0, END)
    else:
        output_label.configure(text='Wrong! answer = {}'.format(z))
        entry.delete(0, END)
        
        

root = Tk()
root.title('Math Game')

label = Label(text='Are you ready to start the game?', font=('verdana', 16))
entry = Entry(font=('verdana', 16), width=1)
answer_button = Button(font=('Verdana', 16), command = answer())
button = Button(text='If ready click me!', font=('verdana', 16), command = math_game)
output_label = Label(font=('verdana', 16))
label.grid(row=1, column=0)
entry.grid(row=1, column=1)
answer_button.grid(row=1, column=4)
button.grid(row=1, column=2)
output_label.grid(row=2, column=0, columnspan=3)

count = 0
i = 0
mainloop()
