from tkinter import *
root = Tk()
root.geometry("346x456")
topframe=Frame(root)
topframe.pack()
bframe=Frame(root)
bframe.pack()
button1=Button(topframe,text="File",fg="blue")
button2=Button(topframe,text="Edit",fg="blue")
button3=Button(topframe,text="View",fg="blue")
button4=Button(topframe,text="Navigate",fg="blue")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
one=Label(root, text="Welcome to GUI",bg="red")
one.pack(side=LEFT,fill=Y,pady=40)
two=Label(root, text="Thanks alot", bg="blue")
two.pack(side=BOTTOM,fill=X,padx=34)
root.mainloop()