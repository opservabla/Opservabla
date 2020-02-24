a = int(input("Unesite prvi broj:"))
b = int(input("Unesite drugi broj:"))
c = int(input("Unesite treci broj:"))
if a > (b + c) or b > (a + b) or c > (a+b):
    print("{}, {} i {} ne mogu biti stranice trougla".format(a, b, c))
else:
    print("{}, {} i {} mogu biti stranice trougla".format(a, b, c))
