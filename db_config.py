import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="testuser",       # new user
        password="test123",    # new password
        database="employee_performance"
    )

