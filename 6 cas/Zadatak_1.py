#Zadatak 1. / Napisati funkciju koja kao agrument prima duzinu liste
# i kao rezultat vraca popunjenu listu celih brojeva (for petlja)

def unosenje_brojeva(n):
    celi_brojevi = []
    for i in range(n):
        unos = int(input("Unesite {}. broj:".format(i+1)))
        celi_brojevi.append(unos)
    return celi_brojevi

n = int(input("Unesite duzinu liste:"))
print(unosenje_brojeva(n))   


