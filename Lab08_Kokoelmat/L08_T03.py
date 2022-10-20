'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 8 tehtävä 3

    ohjelma kysyy kurssien arvosanoja (0,1,2,3,4 ja 5) ja tallentaa ne listaan
    tulostetaan annettujen arvosanojen määrä ja keskiarvo
    syöttäminen lopetetaan kun käyttäjä antaa tyhjän syötteen

'''

# tyhjän listan luonti

arvosanat = []

# while loop lisää annetut arvosanat listaan ja katkaisee loopin kun käyttäjä antaa tyhjän syötteen
## looppi myös tarkastaa antaako käyttäjä 0:n tai positiivisen kokonaisluvun
### myöskään negatiivisia kokonaislukuja ei lisätä listaan ja ohjeistetaan käyttäjää antamaan kokonaisluku 0-5 väliltä
#### tarkistetaan myös antaako käyttäjä desimaalilukuja
##### loopissa on ongelma että jos numeroita annetaan vähintään yksi ja sen jälkeen annetaan kirjain niin syötettä ei enää kysytä

while True:
    try:
        arvosana = int(input("Anna kurssin arvosana (0,1,2,3,4 tai 5): "))

    except ValueError:
        if len(arvosanat) == 0:
            print("Listassa ei ole arvosanoja")
            continue
        break

    if arvosana < 0 or arvosana > 5:
        print("Annoitko varmasti kokonaisluvun 0-5 väliltä?")
    else:
        arvosana >= 0
        arvosanat.append(arvosana)
        continue

# lasketaan annettujen arvosanojen keskiarvo

keskiarvo = sum(arvosanat) / len(arvosanat)

# tulostetaan arvosanojen määrä ja keskiarvo

print("Annettujen arvosanojen määrä: ", len(arvosanat))
print(f"Lukujen keskiarvo on:  {keskiarvo:.1f}")