# domaci zadatak 2.b)
n = int(input("Unesite prvi broj:"))
m = int(input("Unesite drugi broj:"))
k = int(input("Unesite treci broj:"))
brojevi = []
for i in range (m, n+1):
    brojevi.append(i)
print(brojevi[::-k])
                     
"""while i>m and i<n:
    brojevi.append(i)
    i+=1
    
print(brojevi[::-k])"""