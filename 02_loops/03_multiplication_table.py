"""
Q3: Generate and display the multiplication table of a given number up to 10.
"""

def print_multiplication_table(num):
    print(f"--- Multiplication Table for {num} ---")
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1

if __name__ == "__main__":
    print_multiplication_table(7)
