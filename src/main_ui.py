import tkinter as tk
from tkinter import ttk, messagebox
from main import main 
def submit():
    """Handles form submission and calls main function."""
    problem_name = entry.get()
    all_submissions = all_submissions_var.get()

    if not problem_name:
        messagebox.showwarning("⚠️ Input Error", "Please enter a problem name/slug")
        return

    main(problem_name, all_submissions == "True")
    messagebox.showinfo("✅ Success", f"Problem: {problem_name}\nAll Submissions: {all_submissions}")

def on_enter(e):
    submit_btn.config(style="Hover.TButton")

def on_leave(e):
    submit_btn.config(style="TButton")

def center_window(win, width, height):
    """Centers the window on the screen."""
    win.update_idletasks()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    win.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.title("LeetCode Scraper")
win_width, win_height = 520, 380
root.resizable(False, False)  

bg_color = "#2a2d3e"  # Dark theme
frame_bg = "#3c3f55"  # Slightly lighter for contrast
accent_color = "#ff2683"  # Vibrant accent

root.configure(bg=bg_color)
center_window(root, win_width, win_height)

style = ttk.Style()
style.configure("TLabel", font=("Arial", 13, "bold"), background=frame_bg, foreground="white")
style.configure("TButton", font=("Arial", 12, "bold"), padding=6, background=accent_color, foreground="black")
style.configure("Hover.TButton", font=("Arial", 12, "bold"), padding=6, background="white", foreground="black")
style.configure("TCombobox", font=("Arial", 12), padding=5)
style.configure("TEntry", font=("Arial", 12), padding=5)

title_label = ttk.Label(root, text="LeetCode Scraper", font=("Arial", 18, "bold"), foreground=accent_color, background=bg_color)
title_label.pack(pady=20)

frame = tk.Frame(root, bg=frame_bg, bd=5, relief="flat")
frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=250)

ttk.Label(frame, text="🔹 Problem Name/Slug:", background=frame_bg).grid(row=0, column=0, sticky="w", pady=12, padx=10)
entry = ttk.Entry(frame, width=30, style="TEntry")
entry.grid(row=0, column=1, pady=12, padx=10)

ttk.Label(frame, text="📁 All Submissions:", background=frame_bg).grid(row=1, column=0, sticky="w", pady=12, padx=10)
all_submissions_var = tk.StringVar(value="False")
dropdown = ttk.Combobox(frame, textvariable=all_submissions_var, values=["True", "False"], state="readonly", width=10, style="TCombobox")
dropdown.grid(row=1, column=1, pady=12, padx=10)
dropdown.current(1)  

submit_btn = ttk.Button(frame, text="🔥 Submit", command=submit, style="TButton")
submit_btn.grid(row=2, column=0, columnspan=2, pady=20)
submit_btn.bind("<Enter>", on_enter)
submit_btn.bind("<Leave>", on_leave)

root.mainloop()
