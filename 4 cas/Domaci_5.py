# 5. Zadatak:Korisnik unosi dužinu liste,a zatim i elemente liste. Ispisati
# najveći element u listi koji se nalazi na parnoj POZICIJI kao i njegovu poziciju 
lista_brojeva = []
n = int(input("Unesite broj elemenata liste:"))

for i in range(n):
    unos = int(input("Unesite {}. broj:".format(i + 1)))
    lista_brojeva.append(unos)

trMax = lista_brojeva[0]
pozicija_Maxa = 0
for i in range(len(lista_brojeva)):
    if lista_brojeva[i] > trMax and i%2 == 0:
        trMax = lista_brojeva[i]
        pozicija_Maxa = i

print("Najveci element na parnoj poziciji je {}, na poziciji {}.".format(trMax,pozicija_Maxa))