def convert(msg):
    msg = msg.replace(":)", "🙂")
    msg = msg.replace(":(", "🙁")
    return msg



def main():
    msg=input("Write something ")
    msg=convert(msg)

    print(f"{msg}")


main()
