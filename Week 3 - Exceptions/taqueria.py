def main():
    print(orderPlacer())

def orderPlacer():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    dollars = 0
    while True:
        try:
            #To convert the input into title case to match menu items
            item = input("Item: ").title()

            #Increase total everytime a new order is placed
            dollars += menu[item]
            print("Current Total: $" + str(dollars))

            #Raising error if user types item that is not in the menu
            if item not in menu:
                raise KeyError
            
        #Handling potential errors
        except KeyError:
            continue
        except EOFError:
            return ("Grand Total: $"+ str(dollars))

        

main()
