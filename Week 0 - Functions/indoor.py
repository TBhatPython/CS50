#Main function
def main():
    iniString = input("What is the string you would like to convert to lower case?: ")
    print(toLowerCase(iniString))

# To change the string to lowercase
def toLowerCase(toChange):
    return toChange.lower()


main()

