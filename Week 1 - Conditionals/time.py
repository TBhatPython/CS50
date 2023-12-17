def main():
    time = input("What is the time? ")
    convT = convert(time)
    if(7 <= convT <= 8):
        print("breakfast time")
    elif(12 <= convT <= 13):
        print("lunch time")
    elif(18 <= convT < 19):
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return float(hours)


main()