def main():
    plate = input("Plate: ")
    print(isValid(plate))


def isValid(str):
    if (twoLetters(str) and maxLength(str) and numEnd(str) and firstZero(str) and specChar(str)):
        return "Valid"
    else:
        return "Invalid"

# True if first 2 are letters
def twoLetters(str):
    return str[:2].isalpha()


# True if length is lesser than or equal to 6
def maxLength(str):
    return len(str) <= 6 and len(str) >= 2

# True if there are no numbers in the middle
def numEnd(str):
    cond = True
    check = ""
    newStr = str[::-1]
    for i in newStr:
        if i.isalpha():
            break
    check = newStr[newStr.index(i):]
    for j in check:
        if j.isnumeric():
            cond = False
   
    return cond

# True if the first number is not 0
def firstZero(str):
    for i in str:
        if i.isnumeric():
            first = i
            break
    if(int(first) == 0):
        return False
    else:
        return True

#Returns true if there are no special characters
def specChar(str):
    special = ''',.?!"':;()[]{}\\/&*%$#@+=~|^_<>`'''
    for i in str:
        if i in special:
            return False
    return True

main()