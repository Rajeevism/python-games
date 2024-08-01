from tkinter import *
import math
operator = ""


def btnClick(number):
    global operator
    operator = operator + str(number)
    text_input.set(operator)


def btnClear():
    global operator
    operator = ""
    text_input.set("")


def btnEqual():
    try:
        global operator
        sumup = str(eval(operator))
        text_input.set(sumup)
        operator = ""
    except:
        text_input.set(" error ")
        operator = ""


f = open("font", "w")
f.write('Arial bold')
f.close()

f1 = open("font")
a = f1.read().split()
c = a[0]
d = a[1]
f1.close()

cal = Tk()
cal.title("My Calculator......")
cal.geometry("1200x750")
cal.resizable()

operator = ""
text_input = StringVar()
txtDisplay = Entry(cal, font=(c, 40, d), textvariable=text_input,
                   bg='#808080', bd=30, insertwidth=4, justify=RIGHT).grid(columnspan=5)

btn7 = Button(cal, padx=26, bd=15, fg='black', font=(
    c, 30, d), command=lambda: btnClick(7), text="7", bg='#7F7F7F',).grid(row=1, column=0)
btn8 = Button(cal, padx=26, bd=15, fg='black', font=(
    c, 30, d), command=lambda: btnClick(8), text="8", bg='#7F7F7F',).grid(row=1, column=1)
btn9 = Button(cal, padx=26, bd=15, fg='black', font=(
    c, 30, d), command=lambda: btnClick(9), text="9", bg='#7F7F7F',).grid(row=1, column=2)
btnAdd = Button(cal, padx=26, bd=15, fg='black', font=(
    c, 30, d), command=lambda: btnClick("+"), text="+", bg='#98F5FF',).grid(row=1, column=3)
btn4 = Button(cal, padx=26, bd=15, fg='black', font=(
    c, 30, d), command=lambda: btnClick(4), text="4", bg='#7F7F7F',).grid(row=2, column=0)
btn5 = Button(cal, padx=26, bd=15, fg='black', font=(
    c, 30, d), command=lambda: btnClick(5), text="5", bg='#7F7F7F',).grid(row=2, column=1)
btn6 = Button(cal, padx=26, bd=15, fg='black', font=(
    c, 30, d), command=lambda: btnClick(6), text="6", bg='#7F7F7F',).grid(row=2, column=2)
btnSub = Button(cal, padx=26, bd=15, fg='black', font=(
    c, 30, d), command=lambda: btnClick("-"), text="-", bg='#98F5FF',).grid(row=2, column=3)
btn1 = Button(cal, padx=26, bd=15, fg='black', font=(
    c, 30, d), command=lambda: btnClick(1), text="1", bg='#7F7F7F',).grid(row=3, column=0)
btn2 = Button(cal, padx=26, bd=15, fg='black', font=(
    c, 30, d), command=lambda: btnClick(2), text="2", bg='#7F7F7F',).grid(row=3, column=1)
btn3 = Button(cal, padx=26, bd=15, fg='black', font=(
    c, 30, d), command=lambda: btnClick(3), text="3", bg='#7F7F7F',).grid(row=3, column=2)
btnMulti = Button(cal, padx=26, bd=15, fg='black', font=(
    c, 30, d), command=lambda: btnClick("*"), text="×", bg='#98F5FF',).grid(row=3, column=3)
btn0 = Button(cal, padx=26, bd=15, fg='black', font=(
    c, 30, d), command=lambda: btnClick(0), text="0", bg='#7F7F7F',).grid(row=4, column=1)
btnC = Button(cal, padx=26, bd=15, fg='black', font=(c, 30, d),
              command=btnClear, text="C", bg='#98F5FF',).grid(row=4, column=0)
btnEq = Button(cal, padx=26, bd=15, fg='black', font=(c, 30, d),
               command=btnEqual, text="=", bg='#98F5FF',).grid(row=4, column=2)
btnDiv = Button(cal, padx=26, bd=15, fg='black', font=(
    c, 30, d), command=lambda: btnClick("/"), text="÷", bg='#98F5FF',).grid(row=4, column=3)
btndec = Button(cal, padx=26, bd=15, fg='black', font=(
    c, 30, d), command=lambda: btnClick("."), text=".", bg='#98F5FF',).grid(row=5, column=3)
btnsquare = Button(cal, padx=26, bd=15, fg='black', font=(c, 30, d), command=lambda: btnClick(
    "**"), text="x\u1D4F", bg='#98F5FF',).grid(row=5, column=1)


cal.mainloop()
