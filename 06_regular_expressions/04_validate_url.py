"""
Q4: Validate whether a given string is a valid HTTP/HTTPS URL.
"""
import re

def is_valid_url(url):
    pattern = r'^https?:\/\/(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)?$'
    return re.match(pattern, url) is not None

if __name__ == "__main__":
    for link in ["https://www.google.com", "http://example.org/path?arg=1", "ftp://invalid.com", "just_text"]:
        print(f"'{link}' is valid URL:", is_valid_url(link))
