import sys
import os
from tabulate import tabulate
import csv

def main():

    # Verifica il numero di argomenti
    if len(sys.argv) != 2:
        print("Too many command line arguments")
        sys.exit(1)

    # Verifica estensione
    if not sys.argv[1].endswith(".csv"):
        print("The file is not a .csv")
        sys.exit(1)

    # Verifica esistenza file
    if not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)
    try:
        with open(sys.argv[1], "r", newline="" ) as file:
            reader=csv.reader(file)
            table=[row for row in reader] #Converte il Csv in una lista di liste

            #Alternativa
            # table = []
            # for row in reader:
            #     table.append(row)


            print(tabulate(table, headers="firstrow", tablefmt="grid"))

    except Exception:
        print(f"Error reading file: {Exception}")
        sys.exit(1)






if __name__ == "__main__":
    main()
