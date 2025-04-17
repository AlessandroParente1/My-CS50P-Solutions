def main():
    x,y = get_fraction("Fraction: ")
    x= round( x/y * 100)

    if(x <= 1):
        print("E")
    elif (x >= 99):
            print("F")
    else:  print(f"{x}%")


def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            x, y = int(x), int(y)

            if y == 0:
                continue

            if x > y:
                continue
            
            return x,y


        except (ValueError, ZeroDivisionError):
            pass


main()
