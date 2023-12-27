from validator_collection import validators, checkers, errors


def main():
    email = input("Email: ")
    print(valid(email))

def valid(email):
    try:
        validators.email(email)
        return "This is a valid email address"
    except ValueError:
        return "This is not a valid email address"



if __name__ == "__main__":
    main()