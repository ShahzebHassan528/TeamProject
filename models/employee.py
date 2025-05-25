from utils.db import get_db_connection

def insert_employee(name, role, department):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO employees (name, role, department) VALUES (%s, %s, %s)", (name, role, department))
        conn.commit()
        return True
    except Exception as e:
        print("Error:", e)
        return False
    finally:
        conn.close()
