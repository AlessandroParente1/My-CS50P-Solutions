def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #si assicura che siano minimo 2 caratteri e massimo 6 caratteri
    if not (2 <=len(s) <=6):
        return False

    #Controlla che i primi 2 caratteri della stringa siano lettere (a-z)
    if not s[:2].isalpha():
        return False

    #Verifica che non ci siano caratteri speciali
    if not s.isalnum():
        return False

    digit_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not digit_started:
                if char =='0':
                    return False
                digit_started = True
            elif not s[i:].isdigit():
                return False
    return True


main()
