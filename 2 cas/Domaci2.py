godina = int(input("Unesite godinu:"))
mesec = int(input("Unesite redni broj meseca:"))
if mesec == 1:
    print("{} mesec {} godine je januar i ima 31 dan".format(mesec, godina))
elif mesec == 2:
    if godina%400==0 or (godina%4==0 and godina%100!=0):
        print("{} mesec {} godine je februar i ima 29 dana".format(mesec, godina))
    else:
        print("{} mesec {} godine je januar i ima 28 dana".format(mesec, godina))
elif mesec == 3:
    print("{} mesec {} godine je januar i ima 31 dan".format(mesec, godina))
elif mesec == 4:
    print("{} mesec {} godine je januar i ima 30 dana".format(mesec, godina))
elif mesec == 5:
    print("{} mesec {} godine je januar i ima 31 dan".format(mesec, godina))
elif mesec == 6:
    print("{} mesec {} godine je januar i ima 30 dana".format(mesec, godina))
elif mesec == 7:
    print("{} mesec {} godine je januar i ima 31 dan".format(mesec, godina))
elif mesec == 8:
    print("{} mesec {} godine je januar i ima 31 dan".format(mesec, godina))
elif mesec == 9:
    print("{} mesec {} godine je januar i ima 30 dana".format(mesec, godina))
elif mesec == 10:
    print("{} mesec {} godine je januar i ima 31 dan".format(mesec, godina))
elif mesec == 11:
    print("{} mesec {} godine je januar i ima 30 dana".format(mesec, godina))
elif mesec == 12:
    print("{} mesec {} godine je januar i ima 31 dan".format(mesec, godina))
else :
    print("Pogresan unos")