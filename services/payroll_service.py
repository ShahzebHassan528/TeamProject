def generate_payroll(emp_id, month, basic_salary, bonus, deductions):
    net_pay = basic_salary + bonus - deductions
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO payroll (employee_id, month, basic_salary, bonus, deductions, net_pay)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (emp_id, month, basic_salary, bonus, deductions, net_pay))
    conn.commit()
    conn.close()

def get_payroll(emp_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM payroll WHERE employee_id=%s", (emp_id,))
    result = cursor.fetchall()
    conn.close()
    return result
