import sys
import os
from PIL import Image, ImageOps

def main():

    # Verifica il numero di argomenti
    if len(sys.argv) != 3:
        print("Too many command line arguments")
        sys.exit(1)

    extensions= (".jpg",".jpeg",".png")

    # Verifica estensione
    if not sys.argv[1].endswith(extensions) or not sys.argv[2].endswith(extensions):
        print("Both files must be a .csv")
        sys.exit(1)


    # Verifica se i file hanno la stessa estensione
    if os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
        print("Input and output files must have the same extension")
        sys.exit(1)

    # Verifica esistenza file
    if not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)


    try:
        # Apri l'immagine input
        image = Image.open(sys.argv[1])

        # Apri l'immagine della maglietta
        shirt = Image.open("shirt.png")

        # Ridimensiona e ritaglia l'immagine input per adattarla alla maglietta
        image = ImageOps.fit(image, shirt.size)

        # Sovrapponi la maglietta all'immagine
        image.paste(shirt, (0, 0), shirt)

        # Salva l'output
        image.save(sys.argv[2])

    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
