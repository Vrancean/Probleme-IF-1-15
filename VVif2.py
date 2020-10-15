a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if ((a<32000) and (a>0)) and ((b<32000) and (b>0)) and ((c<32000) and (b>0)):
    if ((a+b>=c) and (a+c>=b) and (b+c>=a)): 
        print("DA")
    elif ((a+b<=c) and (a+c<=b) and (b+c<=a)): 
        print("NU")
else:
     print("Numerele nu satisfac condiția" )