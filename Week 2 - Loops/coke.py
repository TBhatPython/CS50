def main():
    #Initializing amount due
    amountDue = 50
    subtraction(amountDue)

def subtraction(due):
    #Initial amount due
    print("Amount Due: ", due)

    #To only run when amount due is greater than 0
    while due > 0:
        coin = int(input("Input Coins: "))

        #If input is not 5, 10 or 25 cents, ask again
        if coin not in [25, 10, 5]:
            continue
        
        #Change value of due
        due -= coin
        if(due > 0):
            print("Amount due: ", due)

    #Calculate change
    change = -due
    print("Change Owed: ", change)


main()