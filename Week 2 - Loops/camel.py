def main():
    #Input for variable name
    camelCase = input("Please input a variable name: ")
    #Print
    print(toSnakeCase(camelCase))


def toSnakeCase(variable):
    #To convert the string into a list
    charList = [char for char in variable]

    #To iterate over every index of the list
    for i in range(len(charList)):

        #Check if index contains capital letter
        if(charList[i].isupper()):
            # Change capital to lowecase and insert "_" before
            charList[i] = charList[i].lower()
            charList.insert(i, '_')
            
    #Convert the list back to a string
    changed = "".join(charList)
    return changed



main()
            