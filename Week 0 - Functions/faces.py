def main():
    iniStr = input("Please input you string: ")
    print(convert(iniStr))


def convert(toChange):
    toChange = toChange.replace(":)", "🙂")
    toChange = toChange.replace(":(", "🙁")

    return toChange

main()