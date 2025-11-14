from db_config import get_connection
from employee import Employee, Performance
from datetime import date

# ---------- Employee CRUD ----------

def add_employee(emp):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO employee (name, dept, email, password) VALUES (%s, %s, %s, %s)"
    values = (emp.name, emp.dept, emp.email, emp.password)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()

def view_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT emp_id, name, dept, email FROM employee")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# ---------- Performance CRUD ----------

def add_performance(perf):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO performance (emp_id, task, rating, remarks, date) VALUES (%s, %s, %s, %s, %s)"
    values = (perf.emp_id, perf.task, perf.rating, perf.remarks, perf.date)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()

def view_performance():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT p.perf_id, e.name, p.task, p.rating, p.remarks, p.date 
                      FROM performance p JOIN employee e ON p.emp_id = e.emp_id""")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# ---------- Admin Login ----------

def check_admin(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM admin WHERE username=%s AND password=%s"
    cursor.execute(sql, (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result is not None

# ---------- Sample Data ----------

def insert_sample_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Insert sample admin
    cursor.execute("SELECT * FROM admin")
    if not cursor.fetchall():
        cursor.execute("INSERT INTO admin (username, password) VALUES (%s, %s)", ("admin", "admin123"))

    # Insert sample employees
    cursor.execute("SELECT * FROM employee")
    if not cursor.fetchall():
        employees = [
            ("Alice", "IT", "alice@example.com", "pass123"),
            ("Bob", "HR", "bob@example.com", "pass123"),
            ("Charlie", "Finance", "charlie@example.com", "pass123")
        ]
        for emp in employees:
            cursor.execute("INSERT INTO employee (name, dept, email, password) VALUES (%s, %s, %s, %s)", emp)

    # Insert sample performance
    cursor.execute("SELECT * FROM performance")
    if not cursor.fetchall():
        performances = [
            (1, "Project A", 85, "Good work", date.today()),
            (2, "Recruitment Drive", 90, "Excellent", date.today()),
            (3, "Budget Analysis", 80, "Satisfactory", date.today())
        ]
        for perf in performances:
            cursor.execute("INSERT INTO performance (emp_id, task, rating, remarks, date) VALUES (%s, %s, %s, %s, %s)", perf)

    conn.commit()
    cursor.close()
    conn.close()
