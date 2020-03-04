# Zadatak 2: Nacrtati slovo A
n = int(input("Unesite dimenziju slova A:"))
for i in range(1,n+1):
    if (i == 1):
        print(n * "*")
        continue
    if i == 3:
            print(n * "*")   
    else:                    
        print("*" + (n-2) * " " + "*")
     
        
# Jel u if u For petlji ne mogu dva uslova da se stave?