import random

FIRST_NUMBER = 0
SECOND_NUMBER = 0

def main():
    level = get_level()
    correct = 10
    for i in range(11):
        num1, num2 = generate_integer(level)
        for i in range(3):
            ans = int(input(f"{num1} + {num2} = "))
            if ans == (num1 + num2):
                break
            else:
                if i == 2:
                    print(num1 + num2)
                    correct -= 1
                else:
                    print("EEE")
                    continue
    print(f"Score: {correct}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if(level in [1, 2, 3]):
                return level
            else:
                raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        num1, num2 = random.randint(0,9), random.randint(0,9)
    elif level == 2:
        num1, num2 = random.randint(10,99), random.randint(10,99)
    else:
        num1, num2 = random.randint(100,999), random.randint(100,999)
    return num1, num2


if __name__ == "__main__":
    main()