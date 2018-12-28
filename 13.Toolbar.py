from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("ROhit")
root.geometry("600x600")

def custom_quit():
    ans = tkinter.messagebox.askokcancel("Are you sure ?","Are you sure you want to cancel this application")
    if ans:
        print("Exit")
        quit()
    
def work():
    print("Hello rohit ")
def rsw():
    print("Resize window")
    root.geometry("330x300")
def nw():
    print("Normal window")
    root.geometry("600x600")
menu1 = Menu(root)
root.config(menu=menu1)
submenu = Menu(menu1)
menu1.add_cascade(label='File',menu=submenu)
submenu.add_command(label="New File",command=work)
submenu.add_command(label="Save as",command=work)
submenu.add_command(label="Save",command=work)
submenu.add_command(label="Exit",command=custom_quit)

submenu2 = Menu(menu1)
menu1.add_cascade(label="Edit",menu=submenu2)
submenu2.add_command(label="Resize window",command=rsw)
submenu2.add_command(label="Normal window",command=nw)

submenu3 = Menu(menu1)
menu1.add_cascade(label="view",menu = submenu3)

submenu4 = Menu(menu1)
menu1.add_cascade(label="Help",menu = submenu4)

submenu5 = Menu(menu1)
menu1.add_cascade(label="Info",menu = submenu5)

#********Tool Bar *******
toolbar = Frame(root,bg="blue")
button = Button(toolbar,text="Insert image",command=rsw)
button.pack(side=LEFT,padx=2,pady=2)
button2 = Button(toolbar,text="Print",command=nw)
button2.pack(side=LEFT,fil=X)


#Status bar **********
label = Label(root,text="Running....",bd=1,anchor=W,relief=SUNKEN)
label.pack(side=BOTTOM,fill=X)



root.mainloop()
