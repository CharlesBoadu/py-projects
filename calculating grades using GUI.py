from tkinter import *

def calc_grade():
    score = int(entry.get())

    if score >= 80 and score <= 100:
        output_label.configure(text='Grade: '+'A')
    elif score >= 75 and score <= 79:
        output_label.configure(text='Grade: '+'B+')
    elif score >= 70 and score <= 74:
        output_label.configure(text='Grade: '+'B-')
    elif score >= 65 and score <= 69:
        output_label.configure(text='Grade: '+'C+')
    elif score >= 60 and score <= 64:
        output_label.configure(text='Grade: '+'C-')
    elif score >= 55 and score <= 59:
        output_label.configure(text='Grade: '+'D+')
    elif score >= 50 and score <= 54:
        output_label.configure(text='Grade: '+'D-')
    else:
        output_label.configure(text='Grade: '+'Fail')

    entry.delete(0, END)

root = Tk()

label = Label(text='Enter your exam score', font=('verdana', 16))
entry = Entry(font=('verdana', 16), width=4)
button = Button(text='Calculate grade', font=('verdana', 8), width = 16, command=calc_grade)
output_label = Label(font=('verdana', 16))
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=0, column=2)
output_label.grid(row=1, column=0, columnspan=3)

mainloop()
