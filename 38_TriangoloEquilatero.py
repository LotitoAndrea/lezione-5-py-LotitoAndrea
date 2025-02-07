lato1 = float(input("inserisci la misura del primo lato "))
lato2 = float(input("inserisci la misura del secondo lato "))
lato3 = float(input("inserisci la misura del terzo lato "))
if lato1 == lato2 and lato2 == lato3:
    print("Il triangolo è equilatero")
elif lato1 == lato2 or lato2 == lato3 or lato1 == lato3:
    print("Il triangolo è isoscele")
else:
    print("Il triangolo è scaleno")