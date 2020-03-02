# 6. Zadatak: Korisnik unosi neki broj, proveriti da li cifre u tom broju 
# predstavljaju palindrom?
 
#1. nacin

broj = int(input("Unesite neki broj:"))
lista_brojeva= []
while broj > 0:
    poslednja_cifra = broj % 10 
    lista_brojeva.append(poslednja_cifra)
    broj = broj // 10
    
obrnuta = lista_brojeva[::-1]

i = 0
if lista_brojeva[i] == obrnuta[i]:
    print("Broj je palindrom.")
else:
    print("Broj nije palindrom")


# 2. nacin

broj = int(input("Unesite neki broj:"))
kopija = broj
u_nazad = 0

if broj <= 0:
    print("Los unos")
    exit(1)
while broj > 0:
    poslednja_cifra = broj % 10
    u_nazad = u_nazad*10 + poslednja_cifra
    broj = broj // 10
print(u_nazad)        
if u_nazad == kopija:
    print("Broj jeste palindorm.")
else:
    print("Broj nije palindorm.")
    