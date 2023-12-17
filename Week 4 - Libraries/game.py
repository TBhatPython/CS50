import random

def main():
    randNum = random.randint(1, 100)
    guesser(randNum)


def guesser(randNum):
    while True:
        try:
            guessNum = int(input("Your guess: "))
            if guessNum < randNum:
                print("Too small!")
            elif guessNum > randNum:
                print("Too large!")
            elif guessNum < 0:
                raise ValueError
            else:
                print("Just right!")
                break
        except ValueError:
            continue


main()
            

