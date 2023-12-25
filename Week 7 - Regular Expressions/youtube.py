import re
import sys

def main():
    print(parse(sys.argv[1]))


def parse(html): 
    matches = re.search(r".+(https?://)(?:www\.)?youtube.com/embed/([\w]+).+", html, re.IGNORECASE)
    if matches:
        return f"{matches.group(1)}youtu.be/{matches.group(2)}"


if __name__ == "__main__":
    main()