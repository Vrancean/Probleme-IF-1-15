am = int(input("dati nr bilelor albe mari: "))
rm = int(input("dati nr bilelor rosii mari: "))
vm = int(input("dati nr bilelor verzi mari: "))
ami = int(input("dati nr bilelor albe mici: "))
rmi = int(input("dati nr bilelor rosii mici: "))
vmi = int(input("dati nr bilelor verzi mici: "))
bmari = am + rm + vm
bmici = ami + rmi + vmi
print("Sunt",bmari + bmici,"bile in total")
if (bmari > bmici):
    print("Bile mari: ",bmari)
elif (bmici > bmari):
    print("Bile mici: ",bmici)
else:
    print("Numarul de bile mari si mici e egal", bmici)
if ((am + ami) > (rm + rmi)) and ((am + ami) > (vm + vmi)):
    print("Bilele albe sunt cele mai multe: ",am + ami)
if ((rm + rmi) > (am + ami)) and ((rm + rmi) > (vm + vmi)):
    print("Bilele rosii sunt cele mai multe: ",rm + rmi)
if ((vm + vmi) > (rm + rmi)) and ((vm + vmi) > (am + ami)):
    print("Bilele verzi sunt cele mai multe: ",vm + vmi)
if ((am + ami) == (rm + rmi)) and ((am + ami) > (vm + vmi)):
    print("Bilele albe si rosii sunt cele mai multe: ",am + ami)
if ((am + ami) > (rm + rmi)) and ((am + ami) == (vm + vmi)):
    print("Bilele albe si verzi sunt cele mai multe: ",am + ami)
if ((vm + vmi) == (rm + rmi)) and ((am + ami) < (vm + vmi)):
    print("Bilele rosii si verzi sunt cele mai multe: ",rm + rmi)
if ((am + ami) == (rm + rmi)) and ((am + ami) == (vm + vmi)):
    print("Numar egal de bile",am + ami)
