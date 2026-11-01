"""
Q2: Extract 10-digit phone numbers in formats like 123-456-7890, (123) 456-7890, or 1234567890.
"""
import re

def extract_phone_numbers(text):
    pattern = r'(?:\(?\d{3}\)?[-.\s]?|\b)\d{3}[-.\s]?\d{4}\b'
    return re.findall(pattern, text)

if __name__ == "__main__":
    text = "Call 123-456-7890 or 9876543210 or (555) 234-5678 for details."
    print("Phone numbers:", extract_phone_numbers(text))
