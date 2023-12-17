def main():
    shoppingList()

def shoppingList():
    dict = {}
    counter = 0
    while True:
        try:
            #To convert the item into all uppercase
            item = input().upper()

            #To add a new item
            if item not in dict:
                counter += 1
                dict.update({item : counter})
                counter = 0
                continue

            ##To increment the amount of an item by 1
            if item in dict:
                dict[item] += 1

        #To escape out of the while loop
        except EOFError:
            for item in dict:
                print(dict[item], item)
            break


main() 