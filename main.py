from tkinter import *

root = Tk()

tx = Label(root, text='Enter a Number')
tx.pack()
inp = Entry(root, width=30)
inp.pack()

tx1 = Label(root, text='Enter a Number')
tx1.pack()
inp1 = Entry(root, width=30)
inp1.pack()


def add_():
    add = int(inp.get()) + int(inp1.get())
    adding = Label(root, text=add)
    adding.pack()


button = Button(root, text='add two number', command=add_)
button.pack()

root.mainloop()
