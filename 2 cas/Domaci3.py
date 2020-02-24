a = int(input("Unesite prvi broj:"))
b = int(input("Unesite drugi broj:"))
zbir = a + b
proizvod = a * b
if  a%2 == 0 and b%3 == 0:
    print("Zbir ova dva broja je {}".format(zbir))
else:
    print("Proizvod ova dva broja je {}".format(proizvod))