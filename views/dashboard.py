import tkinter as tk
from tkinter import ttk
from utils.style import apply_theme
from views import employee_profile, leave, attendance, payroll, performance, department

class DashboardWindow:
    def __init__(self, master, role):
        self.master = master
        self.master.title("Employee Management Dashboard")
        self.master.geometry("400x500")
        apply_theme(self.master)

        ttk.Label(master, text="Welcome to Dashboard", font=("Segoe UI", 14, "bold")).pack(pady=20)

        self.buttons = []

        # Role-based access
        if role in ("admin", "hr"):
            self.add_button("Employee Profile", employee_profile.main)
            self.add_button("Leave Management", leave.main)
            self.add_button("Attendance", attendance.main)
            self.add_button("Payroll", payroll.main)
            self.add_button("Performance Evaluation", performance.main)
            self.add_button("Department Management", department.main)
        elif role == "employee":
            self.add_button("Leave Management", leave.main)
            self.add_button("Attendance", attendance.main)

        ttk.Button(master, text="Logout", command=self.logout).pack(pady=30)

    def add_button(self, text, command):
        btn = ttk.Button(self.master, text=text, width=30, command=command)
        btn.pack(pady=5)
        self.buttons.append(btn)

    def logout(self):
        self.master.destroy()
        from views.login import main as login_main
        login_main()

def main(role="admin"):
    root = tk.Tk()
    DashboardWindow(root, role)
    root.mainloop()
