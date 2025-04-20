import sys
import os
import csv

def main():

    # Verifica il numero di argomenti
    if len(sys.argv) != 3:
        print("Too many command line arguments")
        sys.exit(1)

    # Verifica estensione
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        print("Both files must be a .csv")
        sys.exit(1)

    # Verifica esistenza file
    if not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)

    try:
        students=[]
        with open(sys.argv[1], "r", newline="" ) as file:
            reader=csv.DictReader(file)
            for student in reader:
                last, first = student["name"].rstrip().split(", ")
                students.append({"first": first,"last": last, "house": student["house"]})



        with open(sys.argv[2], "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(students)



    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)






if __name__ == "__main__":
    main()
