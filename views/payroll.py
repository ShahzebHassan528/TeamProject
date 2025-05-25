import tkinter as tk
from tkinter import messagebox
from utils.style import apply_theme
from services.payroll_service import generate_payroll

def main():
    win = tk.Toplevel()
    win.title("Payroll")
    win.geometry("300x200")
    tk.Label(win, text="Payroll of the Month").pack(pady=10)

def payroll_window():
    def handle_generate():
        emp_id = emp_id_entry.get()
        days = int(days_entry.get())
        rate = float(rate_entry.get())
        if generate_payroll(emp_id, days, rate):
            messagebox.showinfo("Success", "Payroll Generated")
        else:
            messagebox.showerror("Error", "Failed")

    win = tk.Tk()
    win.title("Payroll")

    tk.Label(win, text="Employee ID").pack()
    emp_id_entry = tk.Entry(win)
    emp_id_entry.pack()

    tk.Label(win, text="Worked Days").pack()
    days_entry = tk.Entry(win)
    days_entry.pack()

    tk.Label(win, text="Daily Rate").pack()
    rate_entry = tk.Entry(win)
    rate_entry.pack()

    tk.Button(win, text="Generate", command=handle_generate).pack()
    win.mainloop()
