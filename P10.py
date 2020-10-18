gaini = int(input("dati numarul de gaini: "))
boabe = int(input("dati numarul de boabe: "))
if (boabe % gaini == 0):
    print("Fiecare gaina a primit ",boabe // gaini," boabe, iar curcanul nu a primit.")
elif (boabe % gaini !=0):
    if ((boabe % gaini) > (boabe // gaini)):
        print("curcanul a primit cu ",boabe % gaini," boabe mai mult")
    if ((boabe % gaini) < (boabe // gaini)):
        print("Fiecare gaina a primit cu ",boabe // gaini," boabe mai mult")
    else:
        print("Numar egal")
