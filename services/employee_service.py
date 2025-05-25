from utils.db import get_db_connection

def add_employee(name, designation, dept_id, email, phone, address):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO employee (name, designation, department_id, email, phone, address)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (name, designation, dept_id, email, phone, address))
    conn.commit()
    conn.close()

def get_all_employees():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    conn.close()
    return rows
