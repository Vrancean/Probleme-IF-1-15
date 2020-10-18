x=int(input())
y=int(input())
z=int(input())
if((x<y+z) and (y<x+z) and (z<x+y)):
    print("DA")
else:
    print("NU")