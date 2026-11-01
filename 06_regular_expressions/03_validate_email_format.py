"""
Q3: Validate whether a single string is a valid email address.
"""
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    match = re.match(pattern, email)
    return match is not None

if __name__ == "__main__":
    for email in ["test@domain.com", "invalid-email@", "hello@world.co.in", "@nouser.com"]:
        print(f"'{email}' is valid:", is_valid_email(email))
