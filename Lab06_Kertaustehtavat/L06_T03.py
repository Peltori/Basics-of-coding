'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 6 tehtävä 3

    ohjelma kysyy nimiä niin kauan kunnes käyttäjä antaa tyhjän syötteen
    ja tulostaa nimien lukumäärän ja toiselle riville annetut nimet

'''

# tyhjän listan luonti

nimet_lista = []

# while loop silmukasta poistutaan, jos käyttäjä antaa tyhjän syötteen. Muutoin lisätään oppilaan nimi listaan ja jatketaan silmukkaa

while True:
    nimi = input("Anna oppilaan nimi: ")
    if nimi == '':
        break
    else:
        nimet_lista.append(nimi)
        continue


print(f"Oppilaiden lukumäärä:" ,len(nimet_lista))
print(nimet_lista)