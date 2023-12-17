import inflect

nameList = []

#Create and object to access the methods of engine class
x = inflect.engine()

while True:
    try:
        name = input("Name: ").title()

        #Add the given name to the list to be printed later
        nameList.append(name)

    #When you enter Ctrl + Z
    except EOFError:

        #engine.join
        print("Adieu, Adieu, to", ', '.join(nameList))
        break