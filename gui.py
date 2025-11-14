import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from employee import Employee, Performance
from functions import add_employee, view_employees, add_performance, view_performance, check_admin, insert_sample_data
from datetime import date

def launch_gui():
    insert_sample_data()  # Preload sample data

    root = tk.Tk()
    root.title("Employee Performance Management")
    root.geometry("950x500")

    # ---------- Admin Login ----------
    def admin_login():
        username = simpledialog.askstring("Admin Login", "Enter username:")
        password = simpledialog.askstring("Admin Login", "Enter password:")
        if check_admin(username, password):
            messagebox.showinfo("Success", f"Welcome {username}")
            show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid credentials")
            root.destroy()

    # ---------- Main Menu ----------
    def show_main_menu():
        for widget in root.winfo_children():
            widget.destroy()

        tk.Label(root, text="Employee Performance Management", font=("Arial", 16)).pack(pady=10)

        tk.Button(root, text="Employee Management", width=25, command=employee_menu).pack(pady=5)
        tk.Button(root, text="Performance Management", width=25, command=performance_menu).pack(pady=5)
        tk.Button(root, text="Exit", width=25, command=root.destroy).pack(pady=5)

    # ---------- Employee Menu ----------
    def employee_menu():
        for widget in root.winfo_children():
            widget.destroy()

        tk.Label(root, text="Employee Management", font=("Arial", 14)).pack(pady=10)

        tree = ttk.Treeview(root, columns=("ID", "Name", "Dept", "Email"), show="headings")
        for col in ("ID", "Name", "Dept", "Email"):
            tree.heading(col, text=col)
            tree.column(col, width=180)
        tree.pack(pady=10)

        def refresh_employees():
            for row in tree.get_children():
                tree.delete(row)
            for e in view_employees():
                tree.insert("", tk.END, values=e)

        def add_emp_gui():
            name = simpledialog.askstring("Add Employee", "Name:")
            dept = simpledialog.askstring("Add Employee", "Department:")
            email = simpledialog.askstring("Add Employee", "Email:")
            password = simpledialog.askstring("Add Employee", "Password:")
            if name and dept and email and password:
                emp = Employee(name=name, dept=dept, email=email, password=password)
                add_employee(emp)
                messagebox.showinfo("Success", f"Employee {name} added!")
                refresh_employees()

        tk.Button(root, text="Add Employee", width=20, command=add_emp_gui).pack(pady=5)
        tk.Button(root, text="Refresh", width=20, command=refresh_employees).pack(pady=5)
        tk.Button(root, text="Back", width=20, command=show_main_menu).pack(pady=5)

        refresh_employees()

    # ---------- Performance Menu ----------
    def performance_menu():
        for widget in root.winfo_children():
            widget.destroy()

        tk.Label(root, text="Performance Management", font=("Arial", 14)).pack(pady=10)

        tree = ttk.Treeview(root, columns=("ID", "Employee", "Task", "Rating", "Remarks", "Date"), show="headings")
        for col in ("ID", "Employee", "Task", "Rating", "Remarks", "Date"):
            tree.heading(col, text=col)
            tree.column(col, width=130)
        tree.pack(pady=10)

        def refresh_perf():
            for row in tree.get_children():
                tree.delete(row)
            for p in view_performance():
                tree.insert("", tk.END, values=p)

        # ---------- Add Performance with dropdown ----------
        def add_perf_gui():
            employees = view_employees()
            emp_dict = {f"{e[1]} (ID:{e[0]})": e[0] for e in employees}

            emp_window = tk.Toplevel(root)
            emp_window.title("Add Performance")
            emp_window.geometry("300x300")

            tk.Label(emp_window, text="Select Employee:").pack(pady=5)
            emp_var = tk.StringVar()
            emp_var.set(list(emp_dict.keys())[0])
            tk.OptionMenu(emp_window, emp_var, *emp_dict.keys()).pack(pady=5)

            tk.Label(emp_window, text="Task:").pack(pady=5)
            task_entry = tk.Entry(emp_window)
            task_entry.pack(pady=5)

            tk.Label(emp_window, text="Rating (0-100):").pack(pady=5)
            rating_entry = tk.Entry(emp_window)
            rating_entry.pack(pady=5)

            tk.Label(emp_window, text="Remarks:").pack(pady=5)
            remarks_entry = tk.Entry(emp_window)
            remarks_entry.pack(pady=5)

            def submit_perf():
                emp_id = emp_dict[emp_var.get()]
                task = task_entry.get()
                try:
                    rating = int(rating_entry.get())
                except:
                    messagebox.showerror("Error", "Rating must be a number")
                    return
                remarks = remarks_entry.get()
                if emp_id and task and rating is not None and remarks:
                    perf = Performance(emp_id=emp_id, task=task, rating=rating, remarks=remarks, date=date.today())
                    add_performance(perf)
                    messagebox.showinfo("Success", "Performance added!")
                    emp_window.destroy()
                    refresh_perf()

            tk.Button(emp_window, text="Add", command=submit_perf).pack(pady=10)

        tk.Button(root, text="Add Performance", width=20, command=add_perf_gui).pack(pady=5)
        tk.Button(root, text="Refresh", width=20, command=refresh_perf).pack(pady=5)
        tk.Button(root, text="Back", width=20, command=show_main_menu).pack(pady=5)

        refresh_perf()

    admin_login()
    root.mainloop()
