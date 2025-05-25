from models.leave_request import insert_leave_request

def apply_leave(emp_id, start_date, end_date, reason):
    return insert_leave_request(emp_id, start_date, end_date, reason)
