def main():
    print(checkLevel())

def checkLevel():
    while True:
        try:
            fLevel = input("Please input a fraction: ")

            #Splitting the string to new variables x (numerator) and y (denominator)
            x, y = map(float, fLevel.split("/"))

            #To catch Value and Zero division error by raising them
            if x >= y or x == 0:
                raise ValueError
            if y == 0:
                raise ZeroDivisionError
            
            ans = (x/y) * 100

            #Conditions of returning
            if ans >= 99:
                return "Full"
            elif ans <= 1:
                return "Empty"
            else:
                return (str(int(ans)) + "%")

        #After catching potential errors 
        except (ValueError, ZeroDivisionError):
            continue




main()
