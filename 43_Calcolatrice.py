numero1 = float(input("Inserisci un numero: "))
numero2 = float(input("Inserisci un altro numero: "))
operatore = input("Inserisci un operatore  ( +, -, x, : ) : ")
if operatore == "+":
    print("Il risultato è", numero1 + numero2)
elif operatore == "-":
    print("Il risultato è", numero1 - numero2)
elif operatore == "x":
    print("Il risultato è", numero1 * numero2)
elif operatore == ":":
    print("Il risultato è", numero1 / numero2)
else:
    print("Operatore non valido")