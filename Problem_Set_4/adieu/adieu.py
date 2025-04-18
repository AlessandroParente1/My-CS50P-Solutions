import inflect

def main():
    p = inflect.engine()  # Initialize inflect engine
    names = []  # List to store names

    while True:
        try:
            name = input("Name: ")
            names.append(name)


        except EOFError: #Ctrl+D termina il programma
            print()
            break

     # Generate and print the formatted farewell message
    print(f"Adieu, adieu, to {p.join(names)}")


main()
