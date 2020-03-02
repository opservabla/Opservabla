#Zadatak 12 sa casa
broj = int(input("Unesite broj n:"))
lista_brojeva = []
zbir = 0
if broj <= 0:
    print("Pogresan unos.")
    exit(1)
else:
    for i in range(broj):
        unos = int(input("Unesite broj u listu:"))
        lista_brojeva.append(unos)
        if unos < 0 and unos % 2 != 0:
            zbir = zbir + unos
print("Zbir negativnih i neparnih brojeva je {}.".format(zbir))
