from tkinter import *

root = Tk()

textInput = Entry(root, width = 50)
textInput.pack()
#textInput.insert(0,"Send something to the chat")

def clickButton():
    message = textInput.get()
    label = Label(root, text=message)
    label.pack()

button = Button(root, text="Click Me", command=clickButton)
button.pack(side = LEFT)

root.mainloop()