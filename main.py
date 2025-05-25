import tkinter as tk
from views import login

def run_app():
    root = tk.Tk()
    app = login.LoginWindow(root)  # Assumes class-based design in login.py
    root.mainloop()

if __name__ == "__main__":
    run_app()
