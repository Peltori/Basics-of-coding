'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 8 tehtävä 5

    luodaan funktio "lotto()" joka arpoo lottorivin 7 numeroa väliltä 1-40
    palauttaa tämän merkkijonona luvut pilkulla eroteltuina
    käytetään rekisterinumeroa avaimena
    tulostetaan autot aakkosjärjestyksessä rekisterinumeron mukaan

'''

import random


lista = set()

# luodaan funktio joka arpoo seitsemän lukua väliltä 1-40

def lotto():
    for luku in range(7):
        luku = random.randint(1,40)
        lista.add(luku)
        print(lista)

print(lista)

