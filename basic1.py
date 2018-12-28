from tkinter import *
root = Tk()
#everything will be inside this 
#root.mainloop()
#root.minsize(width=344,height=244)
#root.maxsize(width=344,height=244)
root.geometry("344x244")
label = Label(root, text="My first GUI")
label.pack()
root.mainloop()
