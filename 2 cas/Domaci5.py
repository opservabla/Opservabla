# Domaci zadatak 5
a = int(input("Unesite prvi broj:"))
b = int(input("Unesite drugi broj:"))
c = int(input("Unesite treci broj:"))
d = int(input("Unesite cetvrti broj:"))
trMax = a
if b>trMax:
    trMax = b
if c>trMax:
    trMax = c
if d>trMax:
     trMax = d
    
trMin = a
if b<trMin:
    trMin = b
if c<trMin:
    trMin = c
if d<trMin:
     trMin = d  
print("Najveci broj je {}".format(trMax))
print("Najmanji broj je {}".format(trMin))
if trMax % trMin == 0 :
    print("Najveci broj je deljiv sa najmanjim")
else:
    print("Najveci broj nije deljiv sa najmanjim")
