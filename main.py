from src import username, email, handle, is_valid_username

def is_valid_email(email_str):
    # Email criteria: Must contain '@' and '.'
    if "@" in email_str and "." in email_str:
        return True
    return False

def main():
    print("Starting the registration app...")

    # Username loop
    while True:
        user = username()
        if is_valid_username(user):
            print(f"Success! Username saved: {user}")
            break
        else:
            print("invalid username, try again")

    # Email loop
    while True:
        user_email = email()
        if is_valid_email(user_email):
            print(f"Success! Email saved: {user_email}")
            break
        else:
            print("invalid email, try again")

if __name__ == "__main__":
    main()
