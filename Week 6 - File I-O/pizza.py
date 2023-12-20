from tabulate import tabulate
import csv
import sys

def main():
    try:
        if len(sys.argv) != 2:
             sys.exit("Too few command-line arguments")
        if not sys.argv[1].endswith(".csv"):
             sys.exit("Not a CSV file")
        if len(sys.argv) > 2:
             sys.exit("Too many command-line arguments")
        if sys.argv[1] == "sicilian.csv":
            with open("./CSV Files/sicilian.csv", "r") as file:
                data = csv.DictReader(file)
                print(f"Pinocchio’s  Pizza\n {tabulator(data)}")
        elif sys.argv[1] == "regular.csv":
            print("In Regular")
            with open("./CSV Files/regular.csv", "r") as file:
                data = csv.DictReader(file)
                print(f"\nRegular Pizza:\n {tabulator(data)}")
    except FileNotFoundError:
         sys.exit("File not Found")
    

def tabulator(data):
        return tabulate(data, headers = "keys", tablefmt = "grid", numalign = "center")


if __name__ == "__main__":
    main()