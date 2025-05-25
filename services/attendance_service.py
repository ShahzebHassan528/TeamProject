def mark_attendance(emp_id, date, status="Present"):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO attendance (employee_id, date, status)
        VALUES (%s, %s, %s)
    """, (emp_id, date, status))
    conn.commit()
    conn.close()

def get_attendance_by_employee(emp_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM attendance WHERE employee_id=%s", (emp_id,))
    records = cursor.fetchall()
    conn.close()
    return records
