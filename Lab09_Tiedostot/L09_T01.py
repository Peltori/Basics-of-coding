'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 8 tehtävä 5

    ohjelma kysyy käyttäjältä henkilöiden sukunimiä ja kirjoittaa annetut nimet tiedostoon
    nimiä kysytään niin kauan kunnes annetaan tyhjä syöte

'''

# kysytään käyttäjien nimiä

while True:
    nimi = input("Anna sukunimi: ")
    if nimi == '':
        break
    elif nimi.isdigit() or nimi.count("."):
        print("Annoitko varmasti nimen?")
    else:
        file = open(r"tekstitiedostot/testi.txt", "a")
        file.write(nimi + "\n")
        file.close()