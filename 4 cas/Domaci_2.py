# 2. Zadatak:  Korisnik unosi elemente liste sve dok korisnik ne unese -1,
# kada se unese -1 unos elemenata liste prestaje.
# Izracunati sumu svih elemenata liste koji su deljivi sa 4. 
lista_brojeva = []
suma = 0
while True:
    unos = int(input("Unesite neki broj:"))
    if unos == -1:
        break
    lista_brojeva.append(unos)
    if unos % 4 == 0:
        suma = suma + unos
print("Suma brojeva deljivih sa 4 j4 {}.".format(suma))