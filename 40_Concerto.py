print("Mi accompagni al concerto dei Maneskin?")
risposta1=input()
if risposta1=="sì":
    print("Ti va bene se andiamo Sabato?")
    risposta2=input()
    if risposta2 == "sì":
        print("Molto bene, prenoto i biglietti per sabato.")
    else:
        print("Peccato, io sono libero solo sabato :( !")
else:
    print("Allora chiederò a qualcun altro")