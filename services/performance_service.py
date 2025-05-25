from utils.db import get_db_connection

def evaluate_performance(emp_id, period, score, feedback):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO evaluation (employee_id, period, score, feedback)
        VALUES (%s, %s, %s, %s)
    """, (emp_id, period, score, feedback))
    conn.commit()
    conn.close()

def get_evaluations(emp_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM evaluation WHERE employee_id=%s", (emp_id,))
    result = cursor.fetchall()
    conn.close()
    return result
