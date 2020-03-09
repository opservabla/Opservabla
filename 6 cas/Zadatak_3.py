# zadatak 3.: napisati funkciju koja kao argument prima neki broj
# i kao rezultat vraca broj delilaca tog broja

def broj_delilaca(n):
    brojac = 0
    for broj in range(1, n+1):
        if n % broj == 0:
            brojac += 1
    return brojac
n = int(input("Unesite neki broj:"))
print(broj_delilaca(n))                   