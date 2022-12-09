'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Harjoitustyö Tietovisa

    Tietovisassa kysytään 5 monivalinta kysymystä liittyen Linux käyttöjärjestelmään/historiaan
    Kysymykset ovat omassa tiedostossaan "Kysymykset.py"
    Ohjelma arpoo 5 kysymystä satunnaisessa järjestyksessä
    Vastauksien järjestys on myös satunnainen

'''

# Kirjastojen importtaus

import random
from Kysymykset import *
from Funktiot import *

# muuttujien alustusta

pisteet = 0
kysytyt_kysymykset = 0
kysymysten_maara_per_visa = 5

# Pelin aloitus viestit

slowPrint("Tervetuloa Linux-ässä tietovisaan!!", 0.1)

pelaaja = input("Anna pelaajan nimi kiitos: ")

# Arvotaan kysymykset satunnaisesti
## "kysymysten_maara" arpoo 5 kysymystä Kysymykset.py tiedostossa olevista kysymyksistä
### Käytän tässä random.samplea, koska se jättää alkuperäisen listan muuttumattomaan tilaan mutta samalla tekee uuden listan kysymyksistä

kysymysten_maara = min(kysymysten_maara_per_visa, len(dict_kysymykset))
kysymykset = random.sample(list(dict_kysymykset.items()), k=kysymysten_maara)

# Kysymykset sekä vastausvaihtoehdot numeroidaan käyttäjä ystävällisyyden lisäämiseksi ja myös tulosteen selkeyden vuoksi

while True:
    try:
        file = open(r"Harjoitustyö/Pisteet/Visailun_pisteet.txt", "a", encoding = "utf-8")

        for num, (kysymys, vaihtoehdot) in enumerate(kysymykset, start=1):
            slowPrint(f"\nKysymys {num}:")
            slowPrint(f"{kysymys}")
            oikea_vastaus = vaihtoehdot[0]
            arvo_vaihtoehdot = random.sample(vaihtoehdot, k=len(vaihtoehdot))

            for numero, vaihtoehto in enumerate(arvo_vaihtoehdot):
                print(f"  {numero}) {vaihtoehto}")

            vastaus_numero = int(input(f"\nValintasi? "))
            vastaus = arvo_vaihtoehdot[vastaus_numero]

            if vastaus == oikea_vastaus:
                pisteet += 1
                kysytyt_kysymykset += 1
                slowPrint("Oikein!!")

            else:
                slowPrint("Väärin! Parempi onni ensi kerralla")
                kysytyt_kysymykset += 1

        if kysytyt_kysymykset == 5:
            file.write(pelaaja + " Sait " + str(pisteet) + "/5 kysymystä oikein " + "\n" )
            file.close()
            slowPrint("Kiitoksia visailusta ja ensi kertaan!")
            break

# Huomioidaan Index virhe jos käyttäjä yrittää antaa vastausvaihtoehdon mitä ei ole olemassa
## Huomioidaan myös virhe jos käyttäjä ei anna kokonaislukua
### Jos tiedoston luonti ei onnistu ilmoitetaan käyttäjälle asiasta ja breakataan looppi ja ohjelma sammuu
#### Muutoin jäisi tuo printti vain looppaamaan loputtomasti, koska tiedostoa ei löydy ja ohjelma yrittäisi luoda tiedostoa koko ajan uudestaan ja uudestaan

    except IndexError:
        print("Valitsemaasi numeroa ei löytynyt vastauksien valinnasta")

    except ValueError:
        print("Vain kokonaisluvut sallittuja")

    except FileNotFoundError:
        print("Tiedostoa ei löytynyt \nTarkista suorititko ohjelman oikeasta hakemistosta")
        break