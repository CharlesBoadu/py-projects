from tkinter import *
from tkinter.messagebox import *

def pig_latin_translator():
    word = entry.get()
    s = re.split('\s', word)
    translation = []
    
    for i in range(len(s)):
        w = s[i][0]
        t = str(s[i][1:])+' ' +w+'ay'
        translation.append(t)

    translation_in_pig_latin = ' '.join(translation)

    output_label.configure(text='Translation in Pig Latin: '+translation_in_pig_latin)
    entry.delete(0, END)

def quitter_function():
    answer = askquestion(title='Quit', message='Do you really want to close the program')
    if answer == 'yes':
        root.destroy()

root = Tk()
root.title('Pig Latin Translator')
root.protocol('WM_DELETE_WINDOW', quitter_function)

label = Label(text='Enter a word', font=('verdana', 16))
entry = Entry(font=('verdana', 16), width=4)
entry.bind('<Return>', lambda dummy = 0: pig_latin_translator())
button = Button(text='Translate', font=('verdana', 16), command=pig_latin_translator)
output_label = Label(font=('verdana', 16))
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=0, column=2)
output_label.grid(row=1, column=0, columnspan=3)


mainloop()
