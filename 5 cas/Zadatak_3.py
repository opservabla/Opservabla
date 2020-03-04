# Zadatak 3: Nacrtati slovo C
n = int(input("Unesite dimenziju slova C:"))
for i in range(1,n+1):
    if i == 1:
        print(n * "*")
        continue
    if i == n:
        print(n * "*")
    else:
        print("*")