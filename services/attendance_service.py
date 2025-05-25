from models.attendance import insert_attendance

def mark_attendance(emp_id, date, status):
    return insert_attendance(emp_id, date, status)
