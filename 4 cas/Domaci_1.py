# 1.Zadatak: Korisnik unosi listu od 10 elemenata,
# ispisati sve elemente liste pocevsi od pozicije 2 do treće pozicije sa kraja 
# sa korakom 1. (unos preko while petlje)
lista_brojeva = []
i = 0
while i < 10:
    unos= int(input("Unesite {}. elemenat liste:".format(i+1)))
    if unos < 0:  # ovo sam stavila za primer samo pozitivnih brojeva
        print("Pogresan unos.")
        break
    lista_brojeva.append(unos)
    i +=1
print(lista_brojeva[2:-2:1])