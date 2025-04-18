import sys
from pyfiglet import Figlet
import random

def main():

    figlet = Figlet()
    fonts = figlet.getFonts()

    # Check command-line arguments
    if len(sys.argv) == 1:
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font") and sys.argv[2] in fonts:
        font = sys.argv[2]
    else:
        sys.exit("Usage: python figlet.py [-f FONT]")

    figlet.setFont(font=font)
    text = input("Enter text: ")
    print(figlet.renderText(text))


main()
