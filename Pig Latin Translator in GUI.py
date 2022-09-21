from tkinter import *
from tkinter.messagebox import *

def pig_latin_translator():
    word = entry.get()
    s = re.split('\s', word)
    translation = []

    for i in range(len(s)):
        if s[i][0].lower() == 'a' or s[i][0].lower() == 'e' or s[i][0].lower() == 'i' or s[i][0].lower() == 'o' or s[i][0] == 'u':
            t = s[i] + '-yay'
            translation.append(t)
        else:
            for j in range(len(s[i])):
                if s[i][j] == 'a' or s[i][j] == 'e' or s[i][j] == 'i' or s[i][j] == 'o' or s[i][j] == 'u' or s[i][j] == 'y':
                    ind = s[i].index(s[i][j])
                    w = s[i][:ind]
                    t = str(s[i][ind:])+'-'+w+'ay'
                    translation.append(t)
                    break

    translation_in_pig_latin = ' '.join(translation)

    output_label.configure(text='Translation: '+translation_in_pig_latin)
    entry.delete(0, END)

def quitter_function():
    answer = askquestion(title='Quit', message='Do you really want to close the program')
    if answer == 'yes':
        root.destroy()

root = Tk()
root.title('Pig Latin Translator')
root.protocol('WM_DELETE_WINDOW', quitter_function)

label = Label(text='Enter a word or sentence', font=('verdana', 12))
entry = Entry(font=('verdana', 12), width=15)
entry.bind('<Return>', lambda dummy = 0: pig_latin_translator())
button = Button(text='Translate', font=('verdana', 12), command=pig_latin_translator)
output_label = Label(font=('verdana', 12))
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=0, column=2)
output_label.grid(row=1, column=0, columnspan=3)


mainloop()
