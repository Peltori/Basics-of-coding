'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 8 tehtävä 5

    luodaan funktio "lotto()" joka arpoo lottorivin 7 numeroa väliltä 1-40
    palauttaa tämän merkkijonona luvut pilkulla eroteltuina

'''

# otetaan käyttöön "random" kirjasto

import random

# käytetään set tyypin kokoelmaa, koska se ei salli useita samansisältöisiä elementtejä
## tällä eliminoidaan samojen numeroiden mahdollisuus lottorivillä

numerot = set()
lst_numerot = []

# luodaan "lotto()" funktio joka arpoo seitsemän lukua väliltä 1-40
## funktio myös lajittelee numerot pienimmästä suurimpaan

def lotto():    
    while len(numerot) <7:
        luku = random.randint(1,40)
        numerot.add(luku)

    for numero in numerot:
        lst_numerot.append(numero)
    lst_numerot.sort()
    print(lst_numerot)

lotto()