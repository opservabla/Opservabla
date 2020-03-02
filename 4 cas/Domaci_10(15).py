# Zadatak 15 sa casa
# Napisati program koji učitava cele brojeve sve do unosa broja nula, 
# a zatim izračunava i ispisuje aritmetičku sredinu unetih brojeva na četiri decimale.

lista_brojeva = []
zbir = 0
while True:
    unos = int(input("Unesite broj:"))
    if unos == 0:
        if len(lista_brojeva) == 0:
            print("Niste uneli nijedan broj.")
        break
    lista_brojeva.append(unos)
    zbir = zbir + unos

if len(lista_brojeva) != 0 :   
    print("Aritmeticka sredina unetih brojeva je {:.4f}.".format(zbir/len(lista_brojeva)))