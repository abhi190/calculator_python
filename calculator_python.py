from tkinter import *
#creating a window
root = Tk()
root.title("Simple Calculator")
root.iconbitmap(r'C:\Users\aipat\Downloads\calculator.png')


e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx = 10, pady = 10)

def Button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))

def Button_clear():
    e.delete(0, END)

def Button_add():
    first_number= e.get()
    global f_num
    f_num = first_number
    global math 
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def Button_sub():
    first_number= e.get()
    global f_num
    f_num = first_number
    global math 
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def Button_div():
    first_number= e.get()
    global f_num
    f_num = first_number
    global math 
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def Button_mul():
    first_number= e.get()
    global f_num
    f_num = first_number
    global math 
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def Button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number) )

    if math == "subtraction":
        e.insert(0, f_num - int(second_number) )

    if math == "multiplication":
        e.insert(0, f_num * int(second_number) )

    if math == "division":
        e.insert(0, f_num / int(second_number) )

mybutton1 = Button(root, text="1", padx=40, pady = 20, command = lambda:Button_click(1)).grid(row=1, column=0)
mybutton2 = Button(root, text="2",padx=40, pady = 20, command = lambda:Button_click(2)).grid(row=1, column=1)
mybutton3 = Button(root, text="3",padx=40, pady = 20, command = lambda:Button_click(3)).grid(row=1, column=2)

mybutton4 = Button(root, text="4",padx=40, pady = 20, command = lambda:Button_click(4)).grid(row=2, column=0)
mybutton5 = Button(root, text="5",padx=40, pady = 20, command = lambda:Button_click(5)).grid(row=2, column=1)
mybutton6 = Button(root, text="6",padx=40, pady = 20, command = lambda:Button_click(6)).grid(row=2, column=2)

mybutton7 = Button(root, text="7", padx=40, pady = 20, command = lambda:Button_click(7)).grid(row=3, column=0)
mybutton8 = Button(root, text="8", padx=40, pady = 20, command = lambda:Button_click(8)).grid(row=3, column=1)
mybutton9 = Button(root, text="9", padx=40, pady = 20, command = lambda:Button_click(9)).grid(row=3, column=2)

mybutton0 = Button(root, text="0", padx=40, pady = 20, command = lambda:Button_click(0)).grid(row=4, column=1)

mybutton_clear = Button(root, text="C", padx=40, pady = 20, command =Button_clear).grid(row=4, column=0)

mybutton_add = Button(root, text="+", padx=40, pady = 20, command = Button_add).grid(row=4, column=2)
mybutton_sub = Button(root, text="-", padx=40, pady = 20, command = Button_sub).grid(row=1, column=3)
mybutton_mul = Button(root, text="*", padx=40, pady = 20, command = Button_mul).grid(row=2, column=3)
mybutton_div = Button(root, text="/", padx=40, pady = 20, command = Button_div).grid(row=3, column=3)
mybutton_equal = Button(root, text="=", padx=40, pady = 20, command = Button_equal).grid(row=4, column=3)


root.mainloop()
