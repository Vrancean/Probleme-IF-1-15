x = int(input("dati numarul 1: "))
y = int(input("dati numarul 2: "))
if ((x%2==0) and (y%2==0)):
    if (x>y):
        print(x)
    if (y>x):
        print(y)
    else:
        print(x,"",y)
elif ((x%2!=0) and (y%2!=0)):
    print("nu exista numere pare")
elif ((x%2!=0) and (y%2==0)):
    print(y)
elif ((x%2==0) and (y%2!=0)):
    print(x)
