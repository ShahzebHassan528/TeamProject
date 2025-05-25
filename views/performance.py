import tkinter as tk
from tkinter import messagebox
from utils.style import apply_theme
from services.performance_service import evaluate_performance

def main():
    win = tk.Toplevel()
    win.title("Performance")
    win.geometry("300x200")
    tk.Label(win, text="Performance Evaluation").pack(pady=10)

def performance_window():
    def handle_submit():
        emp_id = emp_id_entry.get()
        score = int(score_entry.get())
        feedback = feedback_entry.get()
        if evaluate_performance(emp_id, score, feedback):
            messagebox.showinfo("Success", "Evaluation Submitted")
        else:
            messagebox.showerror("Error", "Failed")

    win = tk.Tk()
    win.title("Performance Evaluation")

    tk.Label(win, text="Employee ID").pack()
    emp_id_entry = tk.Entry(win)
    emp_id_entry.pack()

    tk.Label(win, text="Score (1-10)").pack()
    score_entry = tk.Entry(win)
    score_entry.pack()

    tk.Label(win, text="Feedback").pack()
    feedback_entry = tk.Entry(win)
    feedback_entry.pack()

    tk.Button(win, text="Submit", command=handle_submit).pack()
    win.mainloop()
