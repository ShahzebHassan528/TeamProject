from models.user import get_user_by_username

def authenticate_user(username, password):
    user = get_user_by_username(username)
    if user and user[1] == password:
        return True
    return False
