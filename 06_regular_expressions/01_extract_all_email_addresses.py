"""
Q1: Extract all email addresses from a text using regular expressions.
"""
import re

def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

if __name__ == "__main__":
    sample = "Reach out at user.name@example.com or support@company.org, or admin123@test.co.uk"
    print("Extracted emails:", extract_emails(sample))
