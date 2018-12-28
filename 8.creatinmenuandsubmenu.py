from tkinter import *
root = Tk()
root.geometry("600x800")
def work():
    print("Hello rohit ")

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
root.mainloop()
