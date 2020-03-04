# Zadatak 3. sa slajova (4. cas)
n = int(input("Unesite broj artikala:"))
cene_artikala = []

if n <= 0:
    print("Neispravan unos.")
    
else:
    for i in range(n):
        cena = float(input("Unesite cenu  {}. artikla:".format(i+1)))
        
        if cena > 0:
            cene_artikala.append(cena)
            
        if cena <= 0:
            print("Greska: neispravan unos cene.")
            exit(1)
            
    trMin = cene_artikala[0]
    
    for i in range(len(cene_artikala)):
        if cene_artikala[i] < trMin:
            trMin = cene_artikala[i]
            
    print("Najmanja cena je {:.6f}.".format(trMin))
            
           