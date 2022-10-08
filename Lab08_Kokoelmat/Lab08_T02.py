'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 8 tehtävä 2

    ohjelma kysyy autojen rekisterinumeroita muodossa (ABC-123) ja tallentaa ne listaan
    tulostetaan rekisterinumerot aakkosjärjestyksessä
    syöttäminen lopetetaan silloin kun käyttäjä antaa tyhjän syötteen

'''

# tyhjän listan luonti

rekkarit = []


# while loop lisää annetut nimet listaan ja katkaisee loopin kun käyttäjä antaa tyhjän syötteen

while True:
    rekkari = input("Anna auton rekisterinumero muodossa (ABC-123): ")
    if rekkari == '':
        break
    else:
        rekkarit.append(rekkari)
        continue

# tulostetaan listan sisältö aakkosjärjestyksessä

rekkarit.sort()

print(f"rekisterinumerot aakkosjärjestyksessä: {rekkarit}")