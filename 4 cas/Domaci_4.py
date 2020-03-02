# 4. zadatak: 
# Korisnik unosi dužinu liste,a zatim i elemente liste. 
# Izračunati prosek elemenata koji pri deljenju sa 7 daju ostatak 3. 

lista_brojeva = []
zbir = 0
n = int(input("Unesite broj elemenata liste:"))
for i in range(n):
    unos = int(input("Unesite {}. element liste:".format(i + 1)))
    if unos % 7 == 3:
        lista_brojeva.append(unos)
        zbir = zbir + unos
        delilac = len(lista_brojeva)
print("prosek eprinlemenata koji pri deljenu sa 7 daje ostatak 3 je {:.2f}.".format(zbir/delilac))