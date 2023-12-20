from tabulate import tabulate
import csv

def main():
    with open("sicilian.csv", "r") as file:
        data = csv.DictReader(file)
        print(f"Pinocchio’s  Pizza\n {tabulator(data)}")
    with open("regular.csv", "r") as file:
        data = csv.DictReader(file)
        print(f"\nRegular Pizza:\n {tabulator(data)}")
    

def tabulator(data):
        return tabulate(data, headers = "keys", tablefmt = "grid", numalign = "center")


if __name__ == "__main__":
    main()