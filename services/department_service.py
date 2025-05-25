def add_department(name, manager):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO department (name, manager_name) VALUES (%s, %s)", (name, manager))
    conn.commit()
    conn.close()

def get_departments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM department")
    data = cursor.fetchall()
    conn.close()
    return data
