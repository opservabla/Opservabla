#Zadatak 2. : Napisati funkciju koja kao argument prima duzinu liste i 
# kao rezultat vraca popunjenu listu srtingovima(while petlja)


def lista_stringova(n):
    lista_elemenata = []
    i = 0
    while i < n:
        unos = str(input("Unesite {}. element liste:".format(i+1))) 
        lista_elemenata.append(unos)
        i= i+1
    return lista_elemenata
n = int(input("Unesite broj elemente liste:"))
print(lista_stringova(n))
        