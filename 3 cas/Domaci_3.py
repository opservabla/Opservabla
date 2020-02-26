# Zadatak 3 -> ova lista ili da se nadovezemo na zadatak 2
brojevi = [5,8,11,14,17,20,23,26,29]
zbir = 0
proizvod = 1
for i in brojevi:
    zbir = zbir + i
print("Zbir svih brojeva je {}.".format(zbir))

br_elemenata = len(brojevi)

print("Prosek liste brojeva je {}.".format(zbir/br_elemenata))

for i in brojevi:
    proizvod = proizvod * i
print("Proizvod svih brojeva je {}".format(proizvod))