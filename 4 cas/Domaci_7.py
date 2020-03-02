# 7. Zadatak:Korisnik unosi elemente liste sve dok ne unese broj koji je 
# deljiv sa 13. Izracunati razliku najvećeg i najmanjeg elementa u listi.

lista_brojeva = []
while True:
    broj = int(input("Unesite broj u listu:"))
    if broj % 13 ==0:
        break
    else:
        lista_brojeva.append(broj)
        
print(lista_brojeva)
trMax = lista_brojeva[0]
trMin = lista_brojeva[0]
for i in range(len(lista_brojeva)):
    if lista_brojeva[i]> trMax:
        trMax = lista_brojeva[i]
for i in range(len(lista_brojeva)):
    if lista_brojeva[i] < trMin:
        trMin = lista_brojeva[i]

print("Razlika najveceg i najmanjeg broja je: {} - {} = {}.".format(trMax, trMin, trMax-trMin))
