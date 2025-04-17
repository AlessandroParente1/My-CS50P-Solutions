def main():
    grocery_list={}

    while True:
        try:
            item = input("").strip().title() #Rende l'input case-insensitive

            if item: #Evita stringhe vuote
                grocery_list[item] = grocery_list.get(item, 0) + 1 #conta le occorrenze

        except EOFError: #Ctrl+D termina il programma
            print()
            break

    for item in sorted(grocery_list): #ordine alfabetico
        print(f"{grocery_list[item]} {item.upper()}") #Output in maiuscolo



main()
