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

# while loop lisää annetut nimet listaan ja katkaisee loopin kun 10 nimeä on annettu

while True:
    nimet = input("Anna kaverin nimi: ")
    nimet_laskuri += 1
    kaverit.append(nimet)
    if nimet_laskuri == 10:
        break
    else:
        continue

# tulostetaan listan sisältö samassa järjestyksessä kuin nimet on annettu ja tämän jälkeen käänteisessä järjestyksessä

print(f"Kaverien nimet listassa: {kaverit}")

kaverit.reverse()

print(f"Kaverien nimet käänteissä järjestyksessä: {kaverit}")