import tkinter as tk
from tkinter import messagebox
from utils.style import apply_theme
from services.attendance_service import mark_attendance

def main():
    win = tk.Toplevel()
    win.title("Attendance")
    win.geometry("300x200")
    tk.Label(win, text="Attendance view").pack(pady=10)

def attendance_window():
    def handle_mark():
        emp_id = emp_id_entry.get()
        date = date_entry.get()
        status = status_var.get()
        if mark_attendance(emp_id, date, status):
            messagebox.showinfo("Success", "Marked Attendance")
        else:
            messagebox.showerror("Error", "Error")

    win = tk.Tk()
    win.title("Attendance")

    tk.Label(win, text="Employee ID").pack()
    emp_id_entry = tk.Entry(win)
    emp_id_entry.pack()

    tk.Label(win, text="Date (YYYY-MM-DD)").pack()
    date_entry = tk.Entry(win)
    date_entry.pack()

    tk.Label(win, text="Status").pack()
    status_var = tk.StringVar(value="Present")
    tk.OptionMenu(win, status_var, "Present", "Absent").pack()

    tk.Button(win, text="Mark Attendance", command=handle_mark).pack()
    win.mainloop()
