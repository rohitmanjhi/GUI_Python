from tkinter import *
root = Tk()

root.geometry("344x244")
label1 = Label(root, text="My first GUI")
label1.pack()
label2 = Label(root,text='include color',bg='yellow',fg='blue')
label2.pack()
root.mainloop()
