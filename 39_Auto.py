prezzo = float(input("inserisci prezzo automobile "))
if prezzo > 10000 and prezzo < 20000:
    prezzo = prezzo * 0.95
    contanti = input("vuoi pagare in contanti? Rispondi sì o no ")
    if contanti == "sì":
        prezzo = prezzo - 200
elif prezzo > 20000:
    prezzo = prezzo * 0.9
    contanti = input("vuoi pagare in contanti? Rispondi sì o no ")
    if contanti == "sì":
        prezzo = prezzo - 1000
print("devi pagare", prezzo)