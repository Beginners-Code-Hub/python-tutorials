import tkinter as tk
from tkinter import ttk, messagebox, font

import db

COURSES = ["BSIT", "BSCS", "BSIS", "BSEMC"]

root = tk.Tk()
root.title("Student Records")
root.geometry("1280x720+320+150")
font.nametofont("TkDefaultFont").configure(size=14)
font.nametofont("TkTextFont").configure(size=14)
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", rowheight=34, font=("TkDefaultFont", 13))
style.configure("Treeview.Heading", font=("TkDefaultFont", 13, "bold"))
style.configure("TButton", padding=8)

# ---- Form ----
form = ttk.LabelFrame(root, text="Student", padding=12)
form.pack(side="left", fill="y", padx=12, pady=12)

name_var = tk.StringVar()
course_var = tk.StringVar(value=COURSES[0])
year_var = tk.StringVar(value="1")
email_var = tk.StringVar()

ttk.Label(form, text="Name").grid(row=0, column=0, sticky="w", pady=4)
ttk.Entry(form, textvariable=name_var, width=24).grid(row=0, column=1, pady=4)
ttk.Label(form, text="Course").grid(row=1, column=0, sticky="w", pady=4)
ttk.Combobox(form, textvariable=course_var, values=COURSES,
             state="readonly", width=22).grid(row=1, column=1, pady=4)
ttk.Label(form, text="Year").grid(row=2, column=0, sticky="w", pady=4)
ttk.Spinbox(form, textvariable=year_var, from_=1, to=5,
            width=22).grid(row=2, column=1, pady=4)
ttk.Label(form, text="Email").grid(row=3, column=0, sticky="w", pady=4)
ttk.Entry(form, textvariable=email_var, width=24).grid(row=3, column=1, pady=4)

# ---- Table ----
right = ttk.Frame(root, padding=(0, 12, 12, 12))
right.pack(side="right", fill="both", expand=True)

search_var = tk.StringVar()
ttk.Label(right, text="Search").pack(anchor="w")
ttk.Entry(right, textvariable=search_var).pack(fill="x", pady=(0, 8))

columns = ("id", "name", "course", "year", "email")
table = ttk.Treeview(right, columns=columns, show="headings")
for col, width in zip(columns, (50, 200, 90, 60, 260)):
    table.heading(col, text=col.title())
    table.column(col, width=width)
table.pack(fill="both", expand=True)


def clear_form():
    name_var.set("")
    course_var.set(COURSES[0])
    year_var.set("1")
    email_var.set("")
    table.selection_remove(table.selection())


def read_form():
    name = name_var.get().strip()
    if not name:
        messagebox.showwarning("Missing name", "Please enter a name.")
        return None
    if not year_var.get().isdigit():
        messagebox.showwarning("Wrong year", "Year must be a number.")
        return None
    return name, course_var.get(), int(year_var.get()), email_var.get().strip()


def on_select(event):
    selected = table.selection()
    if selected:
        _, name, course, year, email = table.item(selected[0], "values")
        name_var.set(name)
        course_var.set(course)
        year_var.set(year)
        email_var.set(email)


def update():
    selected = table.selection()
    if not selected:
        messagebox.showinfo("Update", "Select a student first.")
        return
    data = read_form()
    if data:
        db.update_student(selected[0], *data)
        refresh()


def delete():
    selected = table.selection()
    if not selected:
        messagebox.showinfo("Delete", "Select a student first.")
        return
    if messagebox.askyesno("Delete", "Delete this student?"):
        db.delete_student(selected[0])
        refresh()
        clear_form()


table.bind("<<TreeviewSelect>>", on_select)
search_var.trace_add("write", lambda *args: refresh())

# ---- Buttons ----
buttons = ttk.Frame(form)
buttons.grid(row=4, column=0, columnspan=2, pady=(16, 0))
ttk.Button(buttons, text="Add", command=add).pack(fill="x", pady=3)
ttk.Button(buttons, text="Update", command=update).pack(fill="x", pady=3)
ttk.Button(buttons, text="Delete", command=delete).pack(fill="x", pady=3)
ttk.Button(buttons, text="Clear", command=clear_form).pack(fill="x", pady=3)

refresh()
root.mainloop()
