import validators


def main():
    print(validator(input("What's your email address? ").strip()))


def validator(email):

    if validators.email(email) and email.lower().endswith(".edu"):
        return "Valid"
    else:
        return"Invalid"




if __name__ == "__main__":
    main()
