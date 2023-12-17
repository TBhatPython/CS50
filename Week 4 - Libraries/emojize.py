import emoji
import requests

def main():
    toEmoji()



def toEmoji():
    string = input("Input: ")
    print(emoji.emojize(string))


main()