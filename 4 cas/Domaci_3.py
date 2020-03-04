# 3. Zadatak: Korisnik unosi dužinu liste,a zatim i elemente liste. 
# Izracunati proizvod ELEMENATA liste koji se nalaze na 
# NEPARNIM POZICIJAMA u listi. 
lista_brojeva = []
n = int(input("Unesite broj elemenata liste:"))
proizvod = 1
for i in range(n):
    unos = int(input("Unesite {}. element liste:".format(i+1)))
    lista_brojeva.append(unos)
print(lista_brojeva)
neparni = lista_brojeva[1::2]
print(neparni)

for i in range(len(neparni)):
    proizvod = proizvod * neparni[i]
    
print("Proizvod elemenata  na neparnim pozicijama je {}.".format(proizvod))