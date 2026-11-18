def username():
    user_name = input("Please enter your username: ")
    return user_name

def email():
    user_email = input("Please enter your email: ")
    return user_email

def handle():
    user_handle = input("Please enter your handle: ")
    return user_handle

def is_valid_username(name):
    banned_words = ["admin", "root", "moderator", "mod", "null"]
    
    # 1. Check if empty or only whitespace
    if not name or not name.strip():
        return False
        
    # 2. Check if it contains any spaces
    if " " in name:
        return False
        
    # 3. Check against banned words (case-insensitive)
    if name.lower() in banned_words:
        return False
        
    return True
