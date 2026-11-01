"""
Q11: Find common elements present across three different sets without intersection methods.
"""

def common_in_three(s1, s2, s3):
    common = set()
    for x in s1:
        if x in s2 and x in s3:
            common.add(x)
    return common

if __name__ == "__main__":
    a = {1, 2, 3, 4, 5}
    b = {2, 3, 5, 7}
    c = {3, 5, 8, 9}
    print("Common in all 3:", common_in_three(a, b, c))
