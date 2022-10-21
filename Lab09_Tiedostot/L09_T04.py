'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 9 tehtävä 4

    ohjelma lukee nimet tiedostosta "nimet.txt" ja kertoo montako nimeä löytyy
    sekä montako kertaa kukin nimi esiintyy

'''

# luodaan tyhjä dictionary
try:
    nimi_kokoelma = {}
    file = open(r"tekstitiedostot/nimet.txt", "r")

    for nimi in file:
        if nimi in nimi_kokoelma:
            nimi_kokoelma[nimi] = nimi_kokoelma[nimi] + 1
        else:
            nimi_kokoelma[nimi] = 1

    print(f"Nimiä on {len(nimi_kokoelma)}")

    for nimi in nimi_kokoelma:
        print(nimi.rstrip("\n"), ", nimi esiintyy: ", nimi_kokoelma[nimi], " kertaa", sep="")
    
    # suljetaan tiedosto
    
    file.close()

# jos koodi on oikein ja tiedoston polku oikea niin ei pitäisi tulla mitään erroria
except:
    print(f"Tiedoston {file} käsittelyssä tapahtui virhe")
    print("Onko tiedosto olemassa?")