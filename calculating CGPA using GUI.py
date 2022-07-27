from tkinter import *
from tkinter.messagebox import *

def calc_class():
    cgpa = float(entry.get())
    if cgpa>=3.6:
        output_label.configure(text='Class: '+'First Class')
    elif cgpa>=3.0:
        output_label.configure(text='Class: '+'Second Class Upper')
    elif cgpa>=2.5:
        output_label.configure(text='Class: '+'Second Class Lower')
    elif cgpa>=2.0:
        output_label.configure(text='Class: '+'Third Class')
    elif cgpa<2.0:
        output_label.configure(text='Class: '+'Pass')

    entry.delete(0, END)

def quitter_function():
    answer = askquestion(title='Quit', message='Do you really want to quit?')
    if answer == 'yes':
        root.destroy()
        
root = Tk()
root.title('CGPA calculator')
root.protocol('WM_DELETE_WINDOW', quitter_function)
root.bind('<Return>', lambda dummy = 0: calc_class())

message_label = Label(text='Enter your CGPA', font=('Verdana', 16))
entry = Entry(font=('Verdana', 16), width=4)
button = Button(text='calculate', font=('Verdana', 8, 'bold'), width=8, command=calc_class)
output_label = Label(font=('Verdana', 16))
message_label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=0, column=2)
output_label.grid(row=1, column=0, columnspan=3)

mainloop()
