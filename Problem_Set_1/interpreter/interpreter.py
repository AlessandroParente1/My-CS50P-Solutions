expression=input("Expression: ")

x, y, z = expression.split(" ")

if(y == "+"):
    print(float(x) + float(z))
if(y == "-"):
    print(float(x) - float(z))
if(y == "/"):
    print(float(x) / float(z))
if(y == "*"):
    print(float(x) * float(z))
