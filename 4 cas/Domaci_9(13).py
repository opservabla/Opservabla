# Zadatak 13 sa casa
# Napisati program koji učitava cele brojeve sve do unosa broja nula
# i ispisuje proizvod onih unetih brojeva koji su pozitivni
lista_brojeva = []
proizvod = 1

while True:
    unos = int(input("Unesite broj:"))
    if unos == 0:
        if len(lista_brojeva) == 0:
            print("Niste uneli ni jedan broj.")
        break        
    lista_brojeva.append(unos)
    if unos > 0:
        proizvod = proizvod * unos
nova_lista = lista_brojeva
nova_lista.sort()
if len(nova_lista) > 0 and nova_lista[-1] < 0:
    print("Svi uneti brojevi su negativni.")       
elif len(lista_brojeva) != 0:
    print("Proizvod pozitivnih brojeva je {}.".format(proizvod))
