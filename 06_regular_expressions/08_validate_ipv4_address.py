"""
Q8: Validate if a string is a valid IPv4 address (0-255 for each octet).
"""
import re

def is_valid_ipv4(ip):
    octet = r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])'
    pattern = f'^{octet}\.{octet}\.{octet}\.{octet}$'
    return re.match(pattern, ip) is not None

if __name__ == "__main__":
    for ip in ["192.168.1.1", "255.255.255.0", "256.100.0.1", "12.34.56"]:
        print(f"'{ip}' valid IPv4:", is_valid_ipv4(ip))
