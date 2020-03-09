# zadatak 4.: Napisati funkciju koja kao argument prima listu koja kao 
# rezultat vraca koji element ima najvise delilaca iz liste

n = int(input("Unesite broj elemenata liste:"))  
def lista_brojeva(n):
    lista_brojeva = []
    lista_brojaca = []
    for i in range(n):
        unos = int(input("Unesite {}. broj u listu:".format(i + 1)))
        lista_brojeva.append(unos)
        lista_brojaca.append(brojac(unos))
    print(lista_brojeva) #ovi printovi stoje da se testiram
    print(lista_brojaca) # inace znam da su visak :)
    
    trMax = lista_brojaca[0]
    for i in range(n):
        if lista_brojaca[i] > trMax:
            trMax = lista_brojaca[i]
            broj = lista_brojeva[i]
    
    return ('Najvise delilaca ima broj', broj, 'ukupno', trMax)
   
    
def brojac(n):
    brojac = 0
    for broj in range(1, n+1):
        if n % broj == 0:
            brojac += 1
    return brojac  
    
print(lista_brojeva(n))
