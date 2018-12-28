from tkinter import *
root = Tk()
root.geometry("800x600")

def left(event):
    print("You have to click left pointer of Mouse")

def middle(event):
    print("You have to click middle pointer of Mouse")

def right(event):
    print("You have to click right pointer of Mouse")

frame = Frame(root,width=300,height=500)
frame.bind("<Button-1>",left)
frame.bind("<Button-2>",middle)
frame.bind("<Button-3>",right)
frame.pack()
root.mainloop()
