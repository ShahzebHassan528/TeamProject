from utils.db import get_db_connection

def insert_evaluation(emp_id, score, feedback):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO evaluations (emp_id, score, feedback) VALUES (%s, %s, %s)",
                       (emp_id, score, feedback))
        conn.commit()
        return True
    except Exception as e:
        print("Evaluation error:", e)
        return False
    finally:
        conn.close()
