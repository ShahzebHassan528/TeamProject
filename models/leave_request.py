from utils.db import get_db_connection

def insert_leave_request(emp_id, start_date, end_date, reason):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO leave_requests (emp_id, start_date, end_date, reason) VALUES (%s, %s, %s, %s)",
                       (emp_id, start_date, end_date, reason))
        conn.commit()
        return True
    except Exception as e:
        print("Leave error:", e)
        return False
    finally:
        conn.close()
