from tkinter import *
root = Tk()
root.title('Calculator')

view = Entry(root,width=30,borderwidth=5)
view. grid(row=0,column=0,columnspan=3, padx=10,pady=10)

def but_add(frist_number):
    pass

def clr():
    view.delete(0, END)


def number(valu):
    curr = view.get()
    view.delete(0,END)
    view.insert(0,str(curr)+str(valu))



button_1 = Button(root,text='1',padx=30,pady=10,command=lambda :number(1))
button_2 = Button(root,text='2',padx=30,pady=10,command=lambda :number(2))
button_3 = Button(root,text='3',padx=30,pady=10,command=lambda :number(3))
button_4 = Button(root,text='4',padx=30,pady=10,command=lambda :number(4))
button_5 = Button(root,text='5',padx=30,pady=10,command=lambda :number(5))
button_6 = Button(root,text='6',padx=30,pady=10,command=lambda :number(6))
button_7 = Button(root,text='7',padx=30,pady=10,command=lambda :number(7))
button_8 = Button(root,text='8',padx=30,pady=10,command=lambda :number(8))
button_9 = Button(root,text='9',padx=30,pady=10,command=lambda :number(9))
button_0 = Button(root,text='0',padx=30,pady=10,command=lambda :number(0))
button_add = Button(root,text='/',padx=48,pady=10,command=but_add).grid(row=1,column=4)
button_sub = Button(root,text='*',padx=49,pady=10,command=but_add).grid(row=2,column=4)
button_mul = Button(root,text='-',padx=49,pady=10,command=but_add).grid(row=3,column=4)
button_div = Button(root,text='+',padx=49,pady=10,command=but_add).grid(row=4,column=4)
button_cl = Button(root,text='C',padx=48,pady=12,command=clr).grid(row=0,column=4)
button_an = Button(root,text='=',padx=66,pady=10,command=but_add).grid(row=4,column=1,columnspan=2)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)



root.mainloop()