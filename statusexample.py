from tkinter import *
root = Tk()
root.title("ROhit")
root.geometry("600x600")
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
submenu.add_command(label="Exit",command=quit)

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

#Status bar **********
label = Label(root,text="Running....",bd=1,anchor=W,relief=SUNKEN)
label.pack(side=BOTTOM,fill=X)

root.mainloop()
