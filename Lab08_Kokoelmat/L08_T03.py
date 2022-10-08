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

while True:
    try:
        arvosana = int(input("Anna kurssin arvosana (1,2,3,5 tai 5): "))
    except ValueError:
        break
    else:
        arvosanat.append(arvosana)
        continue

# lasketaan annettujen arvosanojen keskiarvo

keskiarvo = sum(arvosanat) / len(arvosanat)

# tulostetaan arvosanojen määrä ja keskiarvo

print("annettujen arvosanojen määrä: ", len(arvosanat))
print(f"Lukujen keskiarvo on:  {keskiarvo}")