def main():
    time = input("What time is it? ")
    time= convert(time)
    if(7<= time <=8):
        print("breakfast time")
    if(12<= time <=13):
        print("lunch time")
    if(18<= time <=19):
        print("dinner time")



def convert(time):
    hour, minutes = time.split(":")
    hour = float(hour)
    minutes = float(minutes)/60
    return hour + minutes


if __name__ == "__main__":
    main()
