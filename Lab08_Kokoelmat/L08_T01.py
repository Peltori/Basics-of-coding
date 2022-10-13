'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 8 tehtävä 1

    ohjelma kysyy kaverien nimiä 10 kappaletta
    tulostetaan nimet ensiksi annetussa järjestyksessä ja tämän jälkeen käänteisessä järjestyksessä

'''

# tyhjän listan luonti
# luodaan laskuri

kaverit = []
nimet_laskuri = 0

'''
    käytin tässä "isidentifier()" string metodia, koska se ei hyväksy numeroilla alkavaa stringia
    mutta hyväksyy kuitenkin numeroita syötteessä muualla kuin alussa, joten tämäkään tapa ei ole täydellinen tarkastamaan
    onko annettu nimi tekstiä vaiko ei, myöskään kaksiosaiset nimet eivät onnistu
    koska jos syötteessä on "-" niin se ei ole silloin identifier

'''
# while loop lisää annetut nimet listaan ja katkaisee loopin kun 10 nimeä on annettu

while True:
    nimet = input("Anna kaverin nimi: ")
    if nimet.isidentifier() == False:
        print("Et antanut nimeä")
    elif nimet_laskuri == 10:
        break
    else:
        nimet_laskuri += 1
        kaverit.append(nimet)

# tulostetaan listan sisältö samassa järjestyksessä kuin nimet on annettu ja tämän jälkeen käänteisessä järjestyksessä

print(f"Kaverien nimet listassa: {kaverit}")

kaverit.reverse()

print(f"Kaverien nimet käänteissä järjestyksessä: {kaverit}")