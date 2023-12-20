import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")

   
    try:
        with open(sys.argv[1], "r") as file:
            file_data = file.read()
            print(f"Lines of code: {count_lines(file_data)}")
    except FileNotFoundError:
        sys.exit("File not found")

def count_lines(data):
    lines = data.split("\n")
    cleaned_lines = []

    for element in lines:
        element = element.rstrip()
        if not (element == "" or "#" in element):
            cleaned_lines.append(element)
    return len(cleaned_lines)


    

    






if __name__ == "__main__":
    main()