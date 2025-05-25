def apply_leave(emp_id, start_date, end_date, reason):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO leave_request (employee_id, start_date, end_date, reason)
        VALUES (%s, %s, %s, %s)
    """, (emp_id, start_date, end_date, reason))
    conn.commit()
    conn.close()

def update_leave_status(leave_id, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE leave_request SET status=%s WHERE id=%s", (status, leave_id))
    conn.commit()
    conn.close()
