'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Harjoitustyö

    Pelissä kysytään kymmenen kysymystä liittyen linux käyttöjärjestelmään/historiaan

'''

# Kirjastojen importtaus

import time
import sys
from Kysymykset import *

# muuttujien alustusta

pisteet = 0

# Listan alustusta

lst_keys = []

# Funktion jolla saadaan tekstin tulostus konsoliin hitaammaksi

def slowPrint(string, speed=0.05):
    for char in string + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

# Pelin aloitus viestit

slowPrint("Tervetuloa Linux ässä tietovisaan", 0.1)

pelaaja = input("Anna pelaajan nimi kiitos: ")

# Arvotaan kysymykset

print(kysymys1)

for key in vastaus1.keys():
    lst_keys.append(key)

# lst_keys.sort()

for key in lst_keys:
    value = vastaus1[key]
    print(key,value)
    vastaus = input("Anna vastaus käytä vain kirjaimia a, b tai c")
    if vastaus == "a" or vastaus == "A":
        print("Vastaus oikein! Sait 5 pistettä")