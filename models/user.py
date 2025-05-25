from utils.db import get_db_connection

def get_user_by_username(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM users WHERE username=%s", (username,))
    result = cursor.fetchone()
    conn.close()
    return result
