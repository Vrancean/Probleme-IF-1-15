x = int(input("dati nota 1: "))
y = int(input("dati nota 2: "))
z = int(input("dati nota 3: "))
if (z>=8):
    print(x,"",y,"",z)
elif (z<8):
    if (x>y):
        print(x)
    if (y>x):
        print(y)
    else:
        print(x,"",y)