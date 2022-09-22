'''
    author Petri Peltomaa
    ohjelmoinnin perusteet: Labra 4 tehtävä 2

    ohjelma kysyy käyttäjältä viikon jokaiselta päivältä sademäärän
    ja laskee sademäärät yhteen

'''

#muuttujien alustus

päivät = 0
viikonsade = 0

# kun kysymykseen on vastattu 7 kertaa lasketaan annetut sademäärät yhteen

while True:
    sademäärä = int(input("Anna sademäärä: "))
    päivät += 1
    viikonsade += sademäärä
    if päivät == 7:
        break

print(f"Viikon sademäärä yhteensä: {viikonsade}")