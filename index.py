import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk
import os


# Database setup
conn = sqlite3.connect('inventory_system.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                name TEXT,
                role TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                dob TEXT,
                email TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS suppliers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                invoice_no TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT,
                quantity INTEGER,
                price REAL)''')
conn.commit()

# Theme setup
def apply_theme(widget):
    style = ttk.Style(widget)
    style.theme_use('clam')
    style.configure("TFrame", background="#d9edf7")
    style.configure("TLabel", background="#d9edf7", font=('Arial', 11))
    style.configure("TButton", font=('Arial', 10, 'bold'))
    style.configure("Treeview", background="#ffffff", fieldbackground="#ffffff", font=('Arial', 10))
    style.configure("Treeview.Heading", font=('Arial', 11, 'bold'))

# GUI setup
root = tk.Tk()
root.title("Inventory Login")
root.geometry("400x400")
apply_theme(root)

# Load icon (optional)
def load_icon(path, size):
    if os.path.exists(path):
        image = Image.open(path)
        image = image.resize(size, Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)
    return None

# Login/Register Frame
login_frame = ttk.Frame(root, padding=20)
login_frame.pack(expand=True)

entry_name = ttk.Entry(login_frame)
entry_name.insert(0, 'Full Name')
entry_name.pack(pady=5)

entry_login_user = ttk.Entry(login_frame)
entry_login_user.insert(0, 'Username')
entry_login_user.pack(pady=5)

entry_login_pass = ttk.Entry(login_frame, foreground='gray')
entry_login_pass.insert(0, 'Password')

def on_focus_in(event):
    if entry_login_pass.get() == 'Password':
        entry_login_pass.delete(0, tk.END)
        entry_login_pass.config(show='*', foreground='black')

def on_focus_out(event):
    if not entry_login_pass.get():
        entry_login_pass.insert(0, 'Password')
        entry_login_pass.config(show='', foreground='gray')

entry_login_pass.bind("<FocusIn>", on_focus_in)
entry_login_pass.bind("<FocusOut>", on_focus_out)
entry_login_pass.pack(pady=5)

role_var = tk.StringVar(value="employee")
role_frame = ttk.Frame(login_frame)
ttk.Label(role_frame, text="Role:").pack(side='left')
ttk.Radiobutton(role_frame, text='Admin', variable=role_var, value='admin').pack(side='left')
ttk.Radiobutton(role_frame, text='Employee', variable=role_var, value='employee').pack(side='left')
ttk.Radiobutton(role_frame, text='Supplier', variable=role_var, value='supplier').pack(side='left')
role_frame.pack(pady=5)

current_user_role = None

def launch_main_app(name, role):
    root.geometry("1000x700")
    root.title("Inventory Management Dashboard")

    for widget in root.winfo_children():
        widget.pack_forget()

    ttk.Label(root, text=f"Welcome, {name} ({role})", font=('Arial', 14, 'bold')).pack(pady=5)
    ttk.Button(root, text="Logout", command=lambda: restart()).pack(pady=5)

    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True, fill='both')

    def restart():
        for widget in root.winfo_children():
            widget.pack_forget()
        root.geometry("400x400")
        login_frame.pack(expand=True)

    def make_tab(label):
        frame = ttk.Frame(notebook, padding=20)
        notebook.add(frame, text=label)
        return frame

    can_view = lambda r: role in r

    if can_view(['admin', 'employee', 'supplier']):
        frame_emp = make_tab('Employees')

        # Search bar
        search_var = tk.StringVar()
        ttk.Entry(frame_emp, textvariable=search_var).grid(row=0, column=0, columnspan=2, sticky='ew', pady=2)
        
        ttk.Label(frame_emp, text="Name:").grid(row=1, column=0)
        name_entry = ttk.Entry(frame_emp)
        name_entry.grid(row=1, column=1)
        ttk.Label(frame_emp, text="DOB:").grid(row=2, column=0)
        dob_entry = ttk.Entry(frame_emp)
        dob_entry.grid(row=2, column=1)
        ttk.Label(frame_emp, text="Email:").grid(row=3, column=0)
        email_entry = ttk.Entry(frame_emp)
        email_entry.grid(row=3, column=1)

        tree = ttk.Treeview(frame_emp, columns=("Name", "DOB", "Email"), show='headings')
        tree.heading("Name", text="Name")
        tree.heading("DOB", text="DOB")
        tree.heading("Email", text="Email")
        tree.grid(row=5, column=0, columnspan=3, sticky='nsew', pady=5)

        def load_employees(filter_text=""):
            tree.delete(*tree.get_children())
            query = "SELECT id, name, dob, email FROM employees WHERE name LIKE ? OR email LIKE ?"
            for row in c.execute(query, (f"%{filter_text}%", f"%{filter_text}%")):
                tree.insert('', tk.END, iid=row[0], values=row[1:])

        search_var.trace("w", lambda *args: load_employees(search_var.get()))

        def delete_selected():
            selected = tree.selection()
            if selected and messagebox.askyesno("Confirm Delete", "Are you sure?"):
                for i in selected:
                    c.execute("DELETE FROM employees WHERE id=?", (i,))
                conn.commit()
                load_employees()

        if role in ['admin', 'employee']:
            def add_employee():
                name, dob, email = name_entry.get(), dob_entry.get(), email_entry.get()
                if name and dob and email:
                    c.execute("INSERT INTO employees (name, dob, email) VALUES (?, ?, ?)", (name, dob, email))
                    conn.commit()
                    name_entry.delete(0, tk.END)
                    dob_entry.delete(0, tk.END)
                    email_entry.delete(0, tk.END)
                    load_employees()
                    messagebox.showinfo("Success", "Employee added.")
                else:
                    messagebox.showwarning("Input Error", "All fields required.")

            ttk.Button(frame_emp, text="Add Employee", command=add_employee).grid(row=4, column=1, pady=5)

        ttk.Button(frame_emp, text="Delete Selected", command=delete_selected).grid(row=4, column=2, padx=5)
        load_employees()

    if can_view(['admin', 'employee', 'supplier']):
        frame_sup = make_tab('Suppliers')

        search_var = tk.StringVar()
        ttk.Entry(frame_sup, textvariable=search_var).grid(row=0, column=0, columnspan=2, sticky='ew', pady=2)

        ttk.Label(frame_sup, text="Supplier Name:").grid(row=1, column=0)
        sup_name = ttk.Entry(frame_sup)
        sup_name.grid(row=1, column=1)
        ttk.Label(frame_sup, text="Invoice No:").grid(row=2, column=0)
        inv_no = ttk.Entry(frame_sup)
        inv_no.grid(row=2, column=1)

        tree_sup = ttk.Treeview(frame_sup, columns=("Name", "Invoice"), show='headings')
        tree_sup.heading("Name", text="Supplier Name")
        tree_sup.heading("Invoice", text="Invoice No")
        tree_sup.grid(row=4, column=0, columnspan=3, sticky='nsew', pady=5)

        def load_suppliers(filter_text=""):
            tree_sup.delete(*tree_sup.get_children())
            query = "SELECT id, name, invoice_no FROM suppliers WHERE name LIKE ? OR invoice_no LIKE ?"
            for row in c.execute(query, (f"%{filter_text}%", f"%{filter_text}%")):
                tree_sup.insert('', tk.END, iid=row[0], values=row[1:])

        search_var.trace("w", lambda *args: load_suppliers(search_var.get()))

        def delete_supplier():
            selected = tree_sup.selection()
            if selected and messagebox.askyesno("Confirm Delete", "Are you sure?"):
                for i in selected:
                    c.execute("DELETE FROM suppliers WHERE id=?", (i,))
                conn.commit()
                load_suppliers()

        if role in ['admin', 'supplier']:
            def add_supplier():
                name, invoice = sup_name.get(), inv_no.get()
                if name and invoice:
                    c.execute("INSERT INTO suppliers (name, invoice_no) VALUES (?, ?)", (name, invoice))
                    conn.commit()
                    sup_name.delete(0, tk.END)
                    inv_no.delete(0, tk.END)
                    load_suppliers()
                    messagebox.showinfo("Success", "Supplier added.")
                else:
                    messagebox.showwarning("Input Error", "All fields required.")

            ttk.Button(frame_sup, text="Add Supplier", command=add_supplier).grid(row=3, column=1, pady=5)

        ttk.Button(frame_sup, text="Delete Selected", command=delete_supplier).grid(row=3, column=2, padx=5)
        load_suppliers()

    if can_view(['admin']):
        frame_users = make_tab('Users')

        search_var = tk.StringVar()
        ttk.Entry(frame_users, textvariable=search_var).grid(row=0, column=0, columnspan=2, sticky='ew', pady=2)

        tree_users = ttk.Treeview(frame_users, columns=("Username", "Name", "Role"), show='headings')
        tree_users.heading("Username", text="Username")
        tree_users.heading("Name", text="Name")
        tree_users.heading("Role", text="Role")
        tree_users.grid(row=1, column=0, columnspan=3, sticky='nsew', pady=5)

        def load_users(filter_text=""):
            tree_users.delete(*tree_users.get_children())
            query = "SELECT id, username, name, role FROM users WHERE username LIKE ? OR name LIKE ? OR role LIKE ?"
            for row in c.execute(query, (f"%{filter_text}%",)*3):
                tree_users.insert('', tk.END, iid=row[0], values=row[1:])

        search_var.trace("w", lambda *args: load_users(search_var.get()))

        def delete_user():
            selected = tree_users.selection()
            if selected and messagebox.askyesno("Confirm Delete", "Are you sure?"):
                for i in selected:
                    c.execute("DELETE FROM users WHERE id=?", (i,))
                conn.commit()
                load_users()

        ttk.Button(frame_users, text="Delete Selected User", command=delete_user).grid(row=2, column=2, pady=5, sticky='e')
        load_users()

def verify_login():
    global current_user_role
    username = entry_login_user.get()
    password = entry_login_pass.get()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    if result:
        current_user_role = result[4]
        login_frame.pack_forget()
        launch_main_app(result[3], current_user_role)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def create_account():
    username = entry_login_user.get()
    password = entry_login_pass.get()
    name = entry_name.get()
    role = role_var.get()
    if username and password and name:
        try:
            c.execute("INSERT INTO users (username, password, name, role) VALUES (?, ?, ?, ?)",
                      (username, password, name, role))
            conn.commit()
            messagebox.showinfo("Success", "Account created. You can now login.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

btn_frame = ttk.Frame(login_frame)
btn_frame.pack(pady=10)
ttk.Button(btn_frame, text="Login", command=verify_login).pack(side='left', padx=5)
ttk.Button(btn_frame, text="Create Account", command=create_account).pack(side='left', padx=5)

# Run App
root.mainloop()
conn.close()
