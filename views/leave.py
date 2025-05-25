import tkinter as tk
from tkinter import messagebox
from utils.style import apply_theme
from services.leave_service import apply_leave

def main():
    win = tk.Toplevel()
    win.title("Leave")
    win.geometry("300x200")
    tk.Label(win, text="Leave Application").pack(pady=10)

def leave_window():
    def handle_apply():
        emp_id = emp_id_entry.get()
        start = start_entry.get()
        end = end_entry.get()
        reason = reason_entry.get()
        if apply_leave(emp_id, start, end, reason):
            messagebox.showinfo("Success", "Leave applied")
        else:
            messagebox.showerror("Error", "Failed")

    win = tk.Tk()
    win.title("Leave Application")

    tk.Label(win, text="Employee ID").pack()
    emp_id_entry = tk.Entry(win)
    emp_id_entry.pack()

    tk.Label(win, text="Start Date (YYYY-MM-DD)").pack()
    start_entry = tk.Entry(win)
    start_entry.pack()

    tk.Label(win, text="End Date (YYYY-MM-DD)").pack()
    end_entry = tk.Entry(win)
    end_entry.pack()

    tk.Label(win, text="Reason").pack()
    reason_entry = tk.Entry(win)
    reason_entry.pack()

    tk.Button(win, text="Apply Leave", command=handle_apply).pack()
    win.mainloop()
