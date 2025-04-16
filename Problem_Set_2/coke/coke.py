print("Amount Due: 50")
n=50

while n > 0:
    coin=int(input("Insert Coin: "))
    if coin in [25,10,5]:
        n=n-coin
        if n >0:
            print("Amount Due: "+ str(n))
        else:
            if n == 0:
                print("Change Owed: 0")
            else:
                print("Change Owed: "+ str(-n))
    else:
        print("Amount Due: "+ str(n))
        continue










