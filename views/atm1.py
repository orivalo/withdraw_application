from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter

root = Tk()

root['bg'] = '#5D6169'
root.title('InfoSuper Bank ATM')
root.geometry('600x400')

root.resizable(width=False, height=False)

frame = Frame(root, bg='#5D6169')
frame.place(relwidth=1, relheight=1)
title = Label(frame, text='Please Insert your Card', bg='#5D6169', font=('Inter', 35, "bold"), )
title.pack(pady=60)
btn = Button(frame, text='Confirm',bg='#658CC2',  font=('Inter', 25), padx=50, pady=50)
btn.pack(pady=60)




root.mainloop()