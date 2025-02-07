print("Benvenuto nel mio programma di conversazione")
print()
risposta=input("Ti piace andare in bicicletta? Rispondi sì o no: ")
if risposta=="sì":
    print("Molto bene! Ti terrai in forma.")
    risposta2 = input("Ti piace anche il basket? ")
    if risposta2=="sì":
        print("Allora sei un atleta!")
    else:
        print("Uno sport è meglio di niente!")
elif risposta == "no":
    risposta3 = input("Ti piace qualche altro sport? Rispondi sì o no: ")
    if risposta3=="sì":
        print("Molto bene! Ti terrai in forma.")
    else:
        print("Non tutti sono sportivi.")