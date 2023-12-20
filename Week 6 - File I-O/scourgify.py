import csv
import sys

students = []

def main():
    try:
        if len(sys.argv) != 3:
            sys.exit("Input 2 command-lines arguments only")
        if not (sys.argv[1].endswith(".csv") or sys.argv[2].endswith(".csv")):
             sys.exit("Both are not CSV files")
        read_before()
        write_after()
    except FileNotFoundError:
        sys.exit("File not found")

def read_before():
    with open("./CSV Files/before.csv", "r") as file:
        data = csv.DictReader(file)
        for row in data:
            name_parts = row['name'].split(",")  
            first_name = name_parts[1].strip()
            last_name = name_parts[0].strip()
            students.append({"firstName": first_name, "lastName": last_name, "house": row['house']})
    return students

def write_after():
    with open(sys.argv[2], "a", newline='') as file:
        fieldnames = ['First Name', 'Last Name', 'House']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for person in students:
            writer.writerow({'First Name': person['firstName'], 'Last Name': person['lastName'], 'House': person['house']})


if __name__ == "__main__":
    main()
    
