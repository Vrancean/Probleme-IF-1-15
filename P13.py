y = int(input("dati locul lui Ionel: "))
if (y <= 100):
    if (y % 4 == 0):
        print("Va primi un tricou negru")
    elif (y % 4 == 1):
        print("Va primi un tricou alb")
    elif (y % 4 == 2):
        print("Va primi un tricou rosu")
    elif (y % 4 == 3):
        print("Va primi un tricou albastru")
else:
    print("Ionel nu va primi un premiu")
