# Zadatak 6.: Napisati funkciju koja kao argument prima listu i dva broja 
# koji predstavljaju pocetnu i krajnju poziciju u listi, 
# koja kao rezultat vraca zbir elemenata izmedju te dve pozicije u listi
n = int(input("Unesite broj elemente liste:"))
def lista_za_proizvod(x, y):
    lista_brojeva = []
    for i in range(n):
        unos = int(input("Unesite {}. element liste:".format(i + 1)))
        lista_brojeva.append(unos)
        nova_lista = lista_brojeva[x:y+1]
        proizvod = 1
        for broj in nova_lista:
            proizvod = proizvod * broj
        
    return proizvod

print(lista_za_proizvod(2, 4))