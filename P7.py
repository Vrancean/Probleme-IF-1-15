x = int(input("dati numarul 1: "))
y = int(input("dati numarul 2: "))
z = int(input("dati numarul 3: "))
if ((x>0)and(y>0)and(z>0)):
    if (y>z):
        print(y)
    if (z>y):
        print(z)
    else:
        print(y,"",z)
else:
    print(x + y)