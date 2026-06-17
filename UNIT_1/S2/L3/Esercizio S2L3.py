# Traccia: Si scriva un programma in Python che in base alla scelta dellʼutente permetta 
# di calcolare il perimetro di diverse figure geometriche (scegliete pure quelle che volete voi). 

while True:
    print("=== CALCOLO DEI PERIMETRI ===")
    print("1. Cerchio (Circonferenza)")
    print("2. Rettangolo")
    print("3. Quadrato")
    print("4. Esci")
    print("=========================")

    scelta = input("Inserisci il numero della figura geometrica desiderata (1-4): ")

    if scelta == "1":
        print("---- Cerchio (Circonferenza) ----")
        raggio = float(input("Inserisci il valore del raggio: "))
        import math
        circonferenza = 2 * math.pi * raggio
        print(f"La Circonferenza del cerchio in esame è: {circonferenza}")

    elif scelta == "2":
        print("----Rettangolo ----")
        altezza = float(input("Inserisci il valore dell'altezza: "))
        base = float(input("Inserisci il valore della base: "))
        perimetro = (base + altezza) * 2
        print(f"Il perimetro del Rettangolo in esame è {perimetro}")


    elif scelta == "3":
        print("--- Quadrato ----")
        lato = float(input("Inserisci la lunghezza del lato: "))
        perimetro = lato * 4
        print(f"Il perimetro del Quadrato in esame è {perimetro}")
    
    elif scelta == "4":
        print("Grazie per aver usato il programma")
        break

    else:
        print("Scelta non valida! Riavvia il programma e inserisci un numero da 1 a 4.")