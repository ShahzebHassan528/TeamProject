from utils.db import get_db_connection

def insert_attendance(emp_id, date, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO attendance (emp_id, date, status) VALUES (%s, %s, %s)",
                       (emp_id, date, status))
        conn.commit()
        return True
    except Exception as e:
        print("Attendance error:", e)
        return False
    finally:
        conn.close()
