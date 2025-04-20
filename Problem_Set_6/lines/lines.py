import sys
import os

def main():

    try:
        # Verifica il numero di argomenti
        if len(sys.argv) != 2:
            print("Too many command line arguments")
            sys.exit(1)

        # Verifica estensione
        if not sys.argv[1].endswith(".py"):
            print("Errore: il file deve avere estensione .py")
            sys.exit(1)

        # Verifica esistenza file
        if not os.path.isfile(sys.argv[1]):
            print("File does not exist")
            sys.exit(1)

        with open(sys.argv[1], "r" ) as file:
            lines = file.readlines()


        i=0

        for line in lines:
            if line.isspace(): #se è vera la condizione
                continue
            elif line.lstrip().startswith("#"): #se è vera la condizione
                continue
            else: i +=1

    finally: print(f"{i}")



if __name__ == "__main__":
    main()
