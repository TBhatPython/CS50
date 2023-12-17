def main():
    x = int(input("What is x: "))
    print("x squared is: " + str(square(x)))

def square(num):
    return pow(num, 2)
main()

