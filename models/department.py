from utils.db import get_db_connection

def insert_department(dept_name, dept_head):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO departments (name, head) VALUES (%s, %s)", (dept_name, dept_head))
        conn.commit()
        return True
    except Exception as e:
        print("Department error:", e)
        return False
    finally:
        conn.close()
