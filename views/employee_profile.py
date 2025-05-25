import tkinter as tk
from tkinter import messagebox
from utils.style import apply_theme
from services.employee_service import add_employee


def main():
    win = tk.Toplevel()
    win.title("Employee Profile")
    win.geometry("300x200")
    tk.Label(win, text="Employee Profile Form").pack(pady=10)

def employee_profile_window():
    def handle_submit():
        name = name_entry.get()
        role = role_entry.get()
        dept = dept_entry.get()
        if add_employee(name, role, dept):
            messagebox.showinfo("Success", "Employee added")
        else:
            messagebox.showerror("Error", "Failed to add employee")

    win = tk.Tk()
    win.title("Add/Edit Employee")

    tk.Label(win, text="Name").pack()
    name_entry = tk.Entry(win)
    name_entry.pack()

    tk.Label(win, text="Role").pack()
    role_entry = tk.Entry(win)
    role_entry.pack()

    tk.Label(win, text="Department").pack()
    dept_entry = tk.Entry(win)
    dept_entry.pack()

    tk.Button(win, text="Submit", command=handle_submit).pack()
    win.mainloop()
