"""
Q12: Create a lambda function to convert Celsius temperature to Fahrenheit (C * 9/5 + 32).
"""

c_to_f = lambda c: (c * 9.0 / 5.0) + 32.0

if __name__ == "__main__":
    for c in [0, 25, 100, -40]:
        print(f"{c}°C = {c_to_f(c)}°F")
