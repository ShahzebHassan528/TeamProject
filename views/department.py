import tkinter as tk
from tkinter import messagebox
from utils.style import apply_theme
from services.department_service import add_department

def main():
    win = tk.Toplevel()
    win.title("Department")
    win.geometry("300x200")
    tk.Label(win, text="Work Department").pack(pady=10)

def department_window():
    def handle_add():
        dept_name = dept_entry.get()
        head = head_entry.get()
        if add_department(dept_name, head):
            messagebox.showinfo("Success", "Department Added")
        else:
            messagebox.showerror("Error", "Failed")

    win = tk.Tk()
    win.title("Department Management")

    tk.Label(win, text="Department Name").pack()
    dept_entry = tk.Entry(win)
    dept_entry.pack()

    tk.Label(win, text="Department Head").pack()
    head_entry = tk.Entry(win)
    head_entry.pack()

    tk.Button(win, text="Add", command=handle_add).pack()
    win.mainloop()
