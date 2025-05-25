from tkinter import ttk

def apply_theme(root):
    style = ttk.Style()
    style.theme_use('clam')  # or 'default', 'alt', 'vista', etc.
    style.configure("TButton", font=('Segoe UI', 10), padding=6)
    style.configure("TLabel", font=('Segoe UI', 11))
    style.configure("TFrame", background="#f0f0f0")

    root.configure(bg="#f0f0f0")
