"""
Q15: Extract all HTML tags and their inner text content.
"""
import re

def extract_tags_and_content(html):
    pattern = r'<([a-zA-Z0-9]+)[^>]*>(.*?)</\1>'
    return re.findall(pattern, html)

if __name__ == "__main__":
    sample = "<h1>Main Heading</h1><p>This is a paragraph.</p><a href='#'>Click Here</a>"
    for tag, content in extract_tags_and_content(sample):
        print(f"Tag: <{tag}>, Content: '{content}'")
