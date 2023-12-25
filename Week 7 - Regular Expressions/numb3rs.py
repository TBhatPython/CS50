import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    index = re.split(r"(?:\.)", ip)
    if len(index) != 4:
        return False
    for i in index:
        if not(0 <= int(i) <= 255):
            return False
    return True

     





if __name__ == "__main__":
    main()