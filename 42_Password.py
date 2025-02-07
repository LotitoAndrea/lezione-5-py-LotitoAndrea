password = "PincoPallino2022!"
tentativi = 2
risposta = input("Inserisci la password: ")
while risposta != password and tentativi != 0:
    tentativi -= 1
    print("Password errata. Tentativi rimasti:", tentativi)
    if tentativi == 0:
        print("Tentativi terminati.")
        break
    risposta = input("Inserisci la password: ")
    if risposta == password:
        print("Password corretta!")
        break