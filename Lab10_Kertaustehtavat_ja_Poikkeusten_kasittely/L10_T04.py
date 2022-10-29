'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 10 tehtävä 4

    alustetaan lista neljällä elementillä ja yritetään muuttaa viidennettä elementtiä jota ei ole olemassa
    lisätään koodiin try except rakenne jolloin koodi ei kaadu ja kerrotaan käyttäjälle miten toimia
    poikkeuksen välttämiseksi

'''

lst_nelja = [1, "A", "B", 10]
try: 
    lst_nelja[4] = 5
    print(lst_nelja)
except:
    print("Listassa ei ole indeksiä 4")