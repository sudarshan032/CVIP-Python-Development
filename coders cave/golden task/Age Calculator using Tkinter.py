import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from tkcalendar import Calendar

def calculate_age():
    try:
        birth_date = calendar.selection_get()
        birth_year = birth_date.year
        birth_month = birth_date.month
        birth_day = birth_date.day

        today = date.today()
        age = today - birth_date

        years = age.days // 365
        months = (age.days % 365) // 30
        days = age.days % 30


        output_window = tk.Toplevel(root)
        output_window.title("Age Result")
        output_window.geometry("250x150")


        years_label = tk.Label(output_window, text=f"Years: {years}")
        years_label.pack(pady=5)
        months_label = tk.Label(output_window, text=f"Months: {months}")
        months_label.pack(pady=5)
        days_label = tk.Label(output_window, text=f"Days: {days}")
        days_label.pack(pady=5)


        close_button = ttk.Button(output_window, text="Close", command=output_window.destroy)
        close_button.pack(pady=10)

    except AttributeError:
        messagebox.showerror("Error", "Please select a valid birth date.")


def check_date():
    if calendar.get_date():
        calculate_button.config(state=tk.NORMAL)
    else:
        calculate_button.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x300")


calendar = Calendar(root, selectmode='day', year=date.today().year)
calendar.place(x=20, y=50, height=180, width=250)
calendar.configure(date_pattern='y-mm-dd')


check_date_button = tk.Button(root, text="Select Date", command=check_date)
check_date_button.place(x=100, y=20)


calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age, state=tk.DISABLED)
calculate_button.place(x=100, y=240)


root.mainloop()
