'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Harjoitustyö Tietovisa

    Tietovisassa kysytään 5 monivalinta kysymystä liittyen linux käyttöjärjestelmään/historiaan
    Kysymykset ovat omassa tiedostossaan "Kysymykset.py"
    Ohjelma arpoo kysymykset satunnaisessa järjestyksessä
    Vastausksien järjestys on myös satunnainnen

'''

# Kirjastojen importtaus

import time
import sys
import random
from Kysymykset import *

# Funktio jolla saadaan tekstin tulostus konsoliin hitaammaksi

def slowPrint(string, speed=0.05):
    for char in string + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

# muuttujien alustusta

pisteet = 0
kysytyt_kysymykset = 0
kysymysten_maara_per_visa = 5

# Pelin aloitus viestit

slowPrint("Tervetuloa Linuxässä tietovisaan!!", 0.1)

pelaaja = input("Anna pelaajan nimi kiitos: ")

# Arvotaan kysymykset

kysymysten_maara = min(kysymysten_maara_per_visa, len(dict_kysymykset))
kysymykset = random.sample(list(dict_kysymykset.items()), k=kysymysten_maara)

while True:
    try:
        for num, (kysymys, vaihtoehdot) in enumerate(kysymykset, start=1):
            slowPrint(f"\nKysymys {num}:")
            slowPrint(f"{kysymys}")
            kysytyt_kysymykset += 1
            oikea_vastaus = vaihtoehdot[0]
            arvo_vaihtoehdot = random.sample(vaihtoehdot, k=len(vaihtoehdot))

            for numero, vaihtoehto in enumerate(arvo_vaihtoehdot):
                print(f"  {numero}) {vaihtoehto}")

            vastaus_numero = int(input(f"\nValintasi? "))
            vastaus = arvo_vaihtoehdot[vastaus_numero]

            if vastaus == oikea_vastaus:
                pisteet += 1
                slowPrint("Oikein!!")
            elif kysytyt_kysymykset == 5:
                break
            else:
                slowPrint("Väärin! Parempi onni ensi kerralla")

    except IndexError:
        print("Valitsemaasi numeroa ei löytynyt vastauksien valinnasta")

    except ValueError:
        print("Vain numerot sallittuja")