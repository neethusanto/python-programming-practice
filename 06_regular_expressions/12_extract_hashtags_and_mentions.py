"""
Q12: Extract all social media hashtags (#tag) and mentions (@user) from a post.
"""
import re

def extract_tags_and_mentions(post):
    hashtags = re.findall(r'#\w+', post)
    mentions = re.findall(r'@\w+', post)
    return hashtags, mentions

if __name__ == "__main__":
    post = "Hey @alex and @sarah, check out #PythonBasics and #CodingChallenge!"
    h, m = extract_tags_and_mentions(post)
    print("Hashtags:", h)
    print("Mentions:", m)
