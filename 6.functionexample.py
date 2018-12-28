from tkinter import *
root = Tk()
root.geometry("600x600")
def hello():
    print("Hello World")

button = Button(root,text="Pint Hello",command=hello)
button.pack()
button2 = Button(root,text="Exit",command=quit)
button2.pack()
root.mainloop()
