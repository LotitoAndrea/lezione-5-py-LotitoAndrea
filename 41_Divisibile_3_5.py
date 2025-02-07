numero = int(input("Inserisci un numero: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("Il numero è divisibile sia per 3 che per 5")
elif numero % 3 == 0:
    print("Il numero è divisibile per 3 ma non per 5")
elif numero % 5 == 0:
    print("Il numero è divisibile per 5 ma non per 3")
else:
    print("Il numero non è divisibile né per 3 né per 5")