# Zadatak 2.a)
brojevi = []
for i in range(5,31):
    brojevi.append(i)
print(brojevi[0:31:3])

zbir = 0
for i in range(brojevi):
    zbir = zbir + i
print(zbir)