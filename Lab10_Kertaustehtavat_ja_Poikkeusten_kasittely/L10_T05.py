'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 10 tehtävä 5

    ohjelma yrittää kirjoittaa tekstitiedoston "ayho.txt" C: aseman juureen (jos Linux macOS tai Unix käyttöjärjestelmä niin käyttäjän juurihakemistoon)
    lisätään koodiin try except rakenne jolloin koodi ei kaadu ja kerrotaan käyttäjälle miten toimia
    poikkeuksen välttämiseksi

'''

# tiedoston kirjoittaminen ei onnistu, koska ohjelmalla ei ole root oikeuksia
try:
    file = open(r"/ayho.txt", "w")
    file.write("Testi tekstiä")
    file.close()
except PermissionError:
    print("Tiedoston kirjoitus epäonnistui, tarvitaan root oikeudet")