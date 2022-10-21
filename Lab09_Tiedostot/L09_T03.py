'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 9 tehtävä 3

    ohjelma kysyy käyttäjältä kokonaislukuja ja tallentaa annetut luvut tiedostoon luvut.txt
    ohjelma lopettaa lukujen kysymisen kun käyttäjä antaa tyhjän syötteen
    viimeisenä ohjelma kirjoittaa montako lukua käyttäjä antoi "Syötetty 5 lukua"

'''

# laskurin määritys ja tiedoston avaaminen

lukujen_maara = 0
file = open(r"tekstitiedostot/luvut.txt", "a")

while True:
    luku = input("Anna kokonaisluku: ")
    if luku == '':
       break
    elif luku.isalpha():
        print("Annoitko varmasti kokonaisluvut?")
    else:
        file.write(luku + "\n")
        lukujen_maara += 1

# kirjoitetaan tiedostoon montako lukua käyttäjä antoi

file.write(f"Syötetty {lukujen_maara} lukua" + "\n")

# suljetaan tiedosto

file.close()