'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 9 tehtävä 1

    ohjelma kysyy käyttäjältä henkilöiden sukunimiä ja kirjoittaa annetut nimet tiedostoon
    nimiä kysytään niin kauan kunnes annetaan tyhjä syöte
    huomioidaan mahdolliset poikkeukset, joita tiedoston käsittely voi aiheuttaa

'''

# määritellään while loop
## looppi tarkistaa löytyykö koodista pisteitä tai numeroita
### isnumeric on True vain silloin jos inputissa KAIKKI merkit ovat numeroita
#### en onnistunut saamaan koodia löytämään merkkien seasta numeroita eli jos jokin merkki on numero niin se tallentuu tiedostoon sellaisenaan

while True:
    try:
        file = open(r"tekstitiedostot/testi.txt", "a")
        nimi = input("Anna sukunimi: ")
        if nimi == '':
            break
        elif nimi.isdigit() or nimi.count("."):
            print("Annoitko varmasti nimen?")
        else:
            file.write(nimi + "\n")
        file.close()
    except:
        print(f"Tiedoston {file} käsittelyssä tapahtui ongelma")
        print("Onko tiedosto varmasti olemassa?")