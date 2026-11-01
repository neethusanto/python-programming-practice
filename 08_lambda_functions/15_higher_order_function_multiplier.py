"""
Q15: Create a higher-order function that returns a lambda multiplier function (closure).
"""

def make_multiplier(n):
    return lambda x: x * n

if __name__ == "__main__":
    double = make_multiplier(2)
    triple = make_multiplier(3)
    
    print("Double 15:", double(15))
    print("Triple 15:", triple(15))
