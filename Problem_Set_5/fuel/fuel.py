def main():
    x = convert("Fraction: ")
    x = gauge(x)
    print(x)




def convert(fraction):
    while True:
        try:
            x, y = input(fraction).split("/")
            x, y = int(x), int(y)

            if y == 0:
                continue

            if x > y:
                continue

            return round( x/y * 100)


        except (ValueError, ZeroDivisionError):
            pass



def gauge(percentage):

    if(percentage <= 1):
        return "E"

    elif (percentage >= 99):
        return "F"

    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
