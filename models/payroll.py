from utils.db import get_db_connection

def insert_payroll(emp_id, days_worked, daily_rate):
    conn = get_db_connection()
    cursor = conn.cursor()
    total_salary = days_worked * daily_rate
    try:
        cursor.execute("INSERT INTO payroll (emp_id, days_worked, daily_rate, total_salary) VALUES (%s, %s, %s, %s)",
                       (emp_id, days_worked, daily_rate, total_salary))
        conn.commit()
        return True
    except Exception as e:
        print("Payroll error:", e)
        return False
    finally:
        conn.close()
