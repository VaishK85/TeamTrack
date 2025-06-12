# main.py

import tkinter as tk
from tkinter import ttk, messagebox, font
from employee import Employee
from utils.qr_generator import generate_qr
from utils.plotter import plot_salary_bonus
from utils.image_utils import update_photo

def center_window(win, width=650, height=550):
    screen_w = win.winfo_screenwidth()
    screen_h = win.winfo_screenheight()
    x = (screen_w // 2) - (width // 2)
    y = (screen_h // 2) - (height // 2)
    win.geometry(f'{width}x{height}+{x}+{y}')

def submit():
    try:
        emp = Employee(
            name_var.get(), id_var.get(),
            joining_var.get(),
            designation_var.get(), promoted_var.get(),
            float(salary_var.get()), float(bonus_var.get()),
            department_var.get(), email_var.get()
        )

        messagebox.showinfo("✅ Employee Info", emp.info())
        img = generate_qr(emp)
        img.show()
        plot_salary_bonus(emp)

    except ValueError:
        messagebox.showerror("❌ Invalid Input", "Salary and Bonus must be numbers.")

root = tk.Tk()
root.title("👨‍💼 Employee Info System")
center_window(root)
root.configure(bg="#e0f7fa")

title_font = font.Font(family="Helvetica", size=18, weight="bold")
label_font = font.Font(family="Arial", size=11)
entry_font = font.Font(family="Arial", size=11)

tk.Label(root, text="👨‍💼 Employee Info Form", font=title_font, bg="#e0f7fa", fg="#333")\
    .grid(row=0, column=0, columnspan=3, pady=(20, 15))

# Variables
name_var = tk.StringVar()
id_var = tk.StringVar()
department_var = tk.StringVar()
email_var = tk.StringVar()
joining_var = tk.StringVar()
designation_var = tk.StringVar()
promoted_var = tk.StringVar()
salary_var = tk.StringVar()
bonus_var = tk.StringVar()
gender_var = tk.StringVar()

fields = [
    ("🆔 Employee ID", id_var),
    ("👤 Name", name_var),
    ("🏢 Department", department_var),
    ("📧 Email", email_var),
    ("📅 Joining Date", joining_var),
    ("💼 Designation", designation_var),
    ("🚀 Promoted To", promoted_var),
    ("💰 Salary", salary_var),
    ("🎁 Bonus", bonus_var),
]

for idx, (label, var) in enumerate(fields, start=1):
    tk.Label(root, text=label, font=label_font, bg="#e0f7fa", anchor='w')\
        .grid(row=idx, column=0, padx=20, pady=5, sticky='w')
    tk.Entry(root, textvariable=var, font=entry_font, width=30, bd=2, relief='groove')\
        .grid(row=idx, column=1, padx=10, pady=5)

tk.Label(root, text="⚧ Gender", font=label_font, bg="#e0f7fa", anchor='w')\
    .grid(row=len(fields)+1, column=0, padx=20, pady=5, sticky='w')
gender_combo = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female"], state="readonly", font=entry_font)
gender_combo.grid(row=len(fields)+1, column=1, padx=10, pady=5)
gender_combo.set("Male")

photo_label = tk.Label(root, text="Loading Photo...", bg="#e0f7fa", width=150, height=150, relief='sunken')
photo_label.grid(row=1, column=2, rowspan=10, padx=20, pady=10)
update_photo(gender_var.get(), photo_label)

gender_combo.bind("<<ComboboxSelected>>", lambda e: update_photo(gender_var.get(), photo_label))

submit_btn = tk.Button(root, text="📤 Submit", font=("Arial", 13, "bold"), bg="#007acc", fg="white",
                       activebackground="#005f99", activeforeground="white", cursor="hand2", command=submit)
submit_btn.grid(row=len(fields)+2, column=0, columnspan=3, pady=30, ipadx=10, ipady=5)
submit_btn.bind("<Enter>", lambda e: submit_btn.config(bg='#005f99'))
submit_btn.bind("<Leave>", lambda e: submit_btn.config(bg='#007acc'))

root.mainloop()
