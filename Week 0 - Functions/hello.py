def sayHello(toName = "world"):
    return "Hello" , toName




def main():
    name = input("What's your name? ")
    print(sayHello(name))


main()