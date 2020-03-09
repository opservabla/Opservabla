# Zadatak 7.: Napisati recenicu koja kao argument prima string 
# koja vraca duzinu stringa5bez koriscenja len)

def duzina_stringa():
    lista_stringova = []
    recenica = str(input("Napisite neku recenicu:"))
    for slovo in recenica:
        lista_stringova.append(slovo)
    brojac = 0
    for i in lista_stringova:
        brojac = brojac + 1
    return brojac
print(duzina_stringa())