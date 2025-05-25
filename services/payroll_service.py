from models.payroll import insert_payroll

def generate_payroll(emp_id, days_worked, daily_rate):
    return insert_payroll(emp_id, days_worked, daily_rate)
