numeroArticoli = int(input("Inserisci il numero di articoli: "))
prezzoArticolo = float(input("Inserisci il prezzo di un articolo: "))
prezzoTotale = numeroArticoli * prezzoArticolo
sconto = 0

if numeroArticoli < 10:
    if prezzoArticolo >= 10:
        sconto = 0.05
    else:
        sconto = 0.02
elif numeroArticoli == 10:
    sconto = 0.10
else:
    if prezzoTotale > 100:
        sconto = 0.50
    elif prezzoTotale == 100:
        sconto = 0.35
    else:
        sconto = 0.30

prezzoScontato = prezzoTotale * (1 - sconto)
print("Il prezzo totale scontato è", prezzoScontato)