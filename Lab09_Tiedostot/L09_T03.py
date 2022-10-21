'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 9 tehtävä 3

    ohjelma kysyy käyttäjältä kokonaislukuja ja tallentaa annetut luvut tiedostoon luvut.txt
    ohjelma lopettaa lukujen kysymisen kun käyttäjä antaa tyhjän syötteen
    viimeisenä ohjelma kirjoittaa montako lukua käyttäjä antoi "Syötetty 5 lukua"

'''

# laskurin määritys ja tiedoston avaaminen

while True:
    try:
        lukujen_maara = 0
        file = open(r"tekstitiedostot/luvut.txt", "a")
        luku = int(input("Anna kokonaisluku: "))

    except ValueError:
        print("Input tyhjä, lopetetaan ohjelma")
        break

    except:
        print(f"Tiedoston {file} käsittelyssä on onglema")
        print("Onko tiedosto varmasti olemassa")

    else:
        numero = str(luku)
        file.write(numero + "\n")
        lukujen_maara += 1

# kirjoitetaan tiedostoon montako lukua käyttäjä antoi

file.write(f"Syötetty {lukujen_maara} lukua" + "\n")

# suljetaan tiedosto

file.close()