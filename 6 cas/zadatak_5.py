#Zadatak 5.: napisati funkciju koja kao argument prima listu, 
# a kao rezultat vraca proizvod neparnih elemenata liste 
# na parnim pozicijama u listi

n = int(input("Unesite broj elemenata liste:"))

def lista_brojeva(n):
    lista_brojeva = []
    for i in range(n):
        unos = int(input("Unesite {}. element liste:".format(i + 1)))
        lista_brojeva.append(unos)
        nova_lista = lista_brojeva[::2]
    print(nova_lista)
    proizvod = 1
    for broj in nova_lista:
        if broj % 2 == 0:
            proizvod = proizvod * broj
    return proizvod

print(lista_brojeva(n))