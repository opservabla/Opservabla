# Zadatak 8.: Napisati funkciju koja kao argument prima listu stringova
# i vraca kao rezultat najkracu rec

def recenica():   
    lista_reci = []
    recenica = str(input("Napisite neku recenicu:"))
    for rec in recenica.split(" "):
        lista_reci.append(rec)
    return lista_reci

def min_duzina(lista_reci):
    trMin = None 
    indeksListe = None
    for i in range(len(lista_reci)):
        lista_slova = lista_reci[i]
        brojac = len(lista_slova)
        if trMin == None:
            trMin = brojac
            indeksListe = i
        elif brojac < trMin:
            trMin = brojac
            indeksListe = i

    return indeksListe 


lista_reci = recenica()
min_indeks = min_duzina(lista_reci)
print("Najmanja rec je: {}, duzine {}".format(lista_reci[min_indeks], 
      len(lista_reci[min_indeks])))