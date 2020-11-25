from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

def buttonClicked():
   mylist.insert(END, "This is line number ")

button = Button(root, text = "Click", command = buttonClicked)
button.pack(side = BOTTOM)



mainloop()