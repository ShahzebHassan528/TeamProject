import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from utils.style import apply_theme
from services.auth import authenticate_user

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x200")

        self.label_username = tk.Label(master, text="Username:")
        self.label_username.pack(pady=5)
        self.entry_username = tk.Entry(master)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(master, text="Password:")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack(pady=5)

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if authenticate_user(username, password):
            self.master.destroy()
            from views import dashboard
            dashboard.main()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials.")
