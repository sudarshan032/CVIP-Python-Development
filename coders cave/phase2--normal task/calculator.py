from tkinter import *
import tkinter.messagebox as tmsg
import math as m
def show_history(event):
    history_text = "\n".join(history)
    tmsg.showinfo("Calculation History", history_text)


class Calculator:
    def __init__(self, txt, r, c, funcName, color="white"):
        self.var = Button(root, text=txt, padx=3, pady=5, fg="black", bg=color, width=10, font=("Helvetica", 12))
        self.var.bind("<Button-1>", funcName)
        self.var.grid(row=r, column=c)

root = Tk()

root.minsize(520, 340)
root.maxsize(520, 340)

root.title("Scientific Calculator")

root.config(bg="light blue")

sc = StringVar()
sc = Entry(root, width=31, textvariable=sc, relief=SUNKEN, font=("Helvetica", 20))
sc.grid(row=0, column=0, columnspan=10, padx=11, pady=12)

history = []

def sciCal(event):
    key = event.widget
    text = key['text']
    val = sc.get()
    if text == "=":
        try:
            res = eval(val)
        except:
            res = "Math Error"
        sc.delete(0, END)
        sc.insert(0, res)
        history.append(f"{val} = {res}")
    else:
        sc.insert(END, text)

def clrscrn(event):
    sc.delete(0, END)

def helper(event):
    help = '''1. For the following functions please enter the number first and then press the required function:
sin, cos, tan, log, ln, √, !, rad, degree, 1/x, π, e 

2. For multiplication with float numbers, say 5*0.4 multiply like 5*4/10'''
    tmsg.showinfo("Help", help)

Calculator("Help", 5, 0, helper)

def abt(event):
    abt = "Thank you for using our app!"
    tmsg.showinfo("About", abt)

# Create number buttons
for i in range(10):
    Calculator(str(i), (i // 3) + 2, (i % 3), sciCal)

Calculator("+", 2, 3, sciCal)
Calculator("-", 3, 3, sciCal)
Calculator("*", 4, 3, sciCal)
Calculator("/", 5, 3, sciCal)
Calculator(".", 5, 1, sciCal)
Calculator("=", 5, 2, sciCal)
Calculator("C", 4, 2, clrscrn)
Calculator("sin", 2, 4, sciCal)
Calculator("cos", 3, 4, sciCal)
Calculator("tan", 4, 4, sciCal)
Calculator("log", 5, 4, sciCal)
Calculator("ln", 2, 5, sciCal)
Calculator("√", 3, 5, sciCal)
Calculator("!", 4, 5, sciCal)
Calculator("rad", 5, 5, sciCal)
Calculator("degree", 2, 6, sciCal)
Calculator("1/x", 3, 6, sciCal)
Calculator("π", 4, 6, sciCal)
Calculator("e", 5, 6, sciCal)
Calculator("History", 6, 0, show_history)
Calculator("About", 6, 1, abt)

root.mainloop()
