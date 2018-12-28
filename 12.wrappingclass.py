from tkinter import *

class Mybutton:
    def __init__(self,master,text):
        frame = Frame(master)
        frame.pack()
        self.printButton = Button(frame,text=text,command=self.print)
        self.printButton.pack()

    def print(self):
        print("This is my code")
if __name__ == '__main__':
    root = Tk()
    Mybutton(root,"Button-1")
    Mybutton(root,"Button-2")
    root.mainloop()
