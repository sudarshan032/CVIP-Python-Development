from tkinter import *
import tkinter.messagebox as tmsg
import math as m

root = Tk()

root.minsize(520, 400)
root.maxsize(520, 400)

root.title("Scientific Calculator")

sc = StringVar()
sc = Entry(root, width=31, textvariable=sc, relief=SUNKEN, font="cosmicsansms 20")
sc.grid(row=0, column=0, columnspan=5, padx=11, pady=12)

history_list = []


def helper():
    help_msg = '''1. For the following functions, please enter the number first and then press the required function:
    sin, cos, tan, log, ln, √, !, rad, degree, 1/x, π, e 

    2. For multiplication with float numbers, say 5*0.4, multiply like 5*4/10'''
    tmsg.showinfo("Help", help_msg)


def abt():
    abt_msg = "Thank you for using our app!"
    tmsg.showinfo("About", abt_msg)


def const():
    const_msg = '''If you press constants like: π and e, 2 times, the result will be the square of that constant. 
    That means the number of times you press the constant, the result will be constant to the power of that number.'''
    tmsg.showinfo("Constants", const_msg)


def record_expression(expression):
    if expression:
        history_list.append(expression)


def show_history():
    history = "\n".join(history_list)
    tmsg.showinfo("History", f"Expression History:\n{history}")


mainmenu = Menu(root)

submenu = Menu(mainmenu, tearoff=0)
submenu.add_command(label="General", command=helper)
submenu.add_command(label="Constants", command=const)
mainmenu.add_cascade(label="Help", menu=submenu)

mainmenu.add_command(label="About", command=abt)
mainmenu.add_command(label="Exit", command=quit)

root.config(menu=mainmenu)


def sciCal(event):
    key = event.widget
    text = key['text']
    val = sc.get()
    sc.delete(0, END)
    if text == "sin":
        sc.insert(0, m.sin(float(val)))
    elif text == "cos":
        sc.insert(0, m.cos(float(val)))
    elif text == "tan":
        sc.insert(0, m.tan(float(val)))
    elif text == "log":
        if float(val) <= 0.00:
            sc.insert(0, "Not Possible")
        else:
            sc.insert(0, m.log10(float(val)))
    elif text == "ln":
        if float(val) <= 0.00:
            sc.insert(0, "Not Possible")
        else:
            sc.insert(0, m.log(float(val)))
    elif text == "√":
        sc.insert(0, m.sqrt(float(val)))
    elif text == "!":
        sc.insert(0, m.factorial(int(val)))
    elif text == "rad":
        sc.insert(0, m.radians(float(val)))
    elif text == "deg":
        sc.insert(0, m.degrees(float(val)))
    elif text == "1/x":
        if val == "0":
            sc.insert(0, "ꝏ")
        else:
            sc.insert(0, 1 / float(val))
    elif text == "π":
        if val == "":
            ans = str(m.pi)
            sc.insert(0, ans)
        else:
            ans = str(float(val) * (m.pi))
            sc.insert(0, ans)
    elif text == "e":
        if val == "":
            sc.insert(0, str(m.e))
        else:
            sc.insert(0, str(float(val) * (m.e)))


def click(event):
    key = event.widget
    text = key['text']
    old_value = sc.get()
    sc.delete(0, END)
    new_value = old_value + text
    sc.insert(0, new_value)


def clr(event):
    sc.delete(0, END)


def backspace(event):
    entered = sc.get()
    length = len(entered) - 1
    sc.delete(length, END)



def calculate(event):
    expression = sc.get()
    if "^" in expression:
        expression = expression.replace("^", "**")
    try:
        result = eval(expression)
        sc.delete(0, END)
        sc.insert(0, result)
        record_expression(expression + " = " + str(result))
    except Exception as e:
        sc.delete(0, END)
        sc.insert(0, "Error")
        record_expression(expression + " = Error")

class Calculator:
    def __init__(self, txt, r, c, func_name):
        self.var = Button(root, text=txt, padx=3, pady=5, fg="black", bg="white", width=10, font="cosmicsansms 12")
        self.var.bind("<Button-1>", func_name)
        self.var.grid(row=r, column=c)


btn0 = Calculator("sin", 1, 0, sciCal)
btn1 = Calculator("cos", 1, 1, sciCal)
btn2 = Calculator("tan", 1, 2, sciCal)
btn3 = Calculator("log", 1, 3, sciCal)
btn4 = Calculator("ln", 1, 4, sciCal)

btn5 = Calculator("(", 2, 0, click)
btn6 = Calculator(")", 2, 1, click)
btn7 = Calculator("^", 2, 2, click)
btn8 = Calculator("√", 2, 3, sciCal)
btn9 = Calculator("!", 2, 4, sciCal)

btn10 = Calculator("π", 3, 0, sciCal)
btn11 = Calculator("1/x", 3, 1, sciCal)
btn12 = Calculator("deg", 3, 2, sciCal)
btn13 = Calculator("rad", 3, 3, sciCal)
btn14 = Calculator("e", 3, 4, sciCal)

btn15 = Calculator("/", 4, 0, click)
btn16 = Calculator("*", 4, 1, click)
btn17 = Calculator("-", 4, 2, click)
btn18 = Calculator("+", 4, 3, click)
btn19 = Calculator("%", 4, 4, click)

btn20 = Calculator("9", 5, 0, click)
btn21 = Calculator("8", 5, 1, click)
btn22 = Calculator("7", 5, 2, click)
btn23 = Calculator("6", 5, 3, click)
btn24 = Calculator("5", 5, 4, click)

btn25 = Calculator("4", 6, 0, click)
btn26 = Calculator("3", 6, 1, click)
btn27 = Calculator("2", 6, 2, click)
btn28 = Calculator("1", 6, 3, click)
btn29 = Calculator("0", 6, 4, click)

btn30 = Calculator("C", 7, 0, clr)
btn31 = Calculator("⌦", 7, 1, backspace)
btn32 = Calculator("00", 7, 2, click)
btn33 = Calculator(".", 7, 3, click)
btn34 = Calculator("=", 7, 4, calculate)

history_btn = Button(root, text="History", padx=3, pady=5, fg="black", bg="white", width=10, font="cosmicsansms 12",
                     command=show_history)
history_btn.grid(row=8, column=0, columnspan=5, padx=11, pady=5)

root.mainloop()
