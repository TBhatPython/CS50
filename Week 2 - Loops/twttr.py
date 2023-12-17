def main():
    userStr = input("Your tweet: ")
    noVowels(userStr)

def noVowels(str):

    #Vowels that will be used in translation table
    vowels = "aeiouAEIOU"

    #Make a translation table ("to insert", "correspoding to inserted chars", "to remove")
    translationTable = str.maketrans("", "", vowels)

    #Use translation table
    changed = str.translate(translationTable)

    print(changed)
main()