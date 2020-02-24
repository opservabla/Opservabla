# Domaci zadatak 1
temperatura = float(input("Unesite temeraturu u stepenima celzijusa"))
if temperatura < -273.15:
    print("Temperatua od {} stepeni je neispravna, ne moze biti niza od apsolutne nule".format(temperatura))
elif temperatura == -273.15:
    print("Temperatura od {} stepeni je na apsolutnoj nuli".format(temperatura))
elif temperatura > -273.15 and temperatura < 0:
    print("Temperatura od {}  stepeni je ispod tacke mrznjenja".format(temperatura))
elif temperatura == 0:
    print("Temperatura od {} stepeni je na tacki mrznjenja".format(temperatura))
elif temperatura > 0 and temperatura < 100:
    print("Temperatura od {} stepeni je u normalnom opsegu".format(temperatura))
elif temperatura == 100:
    print("Temeratura od {} stepeni je na tacki vrenja".format(temperatura))
elif temperatura > 100:
    print("Temperatura od {} je iznad tacke vrenja".format(temperatura))