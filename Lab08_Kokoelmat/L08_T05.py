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

# luodaan "lotto()" funktio joka arpoo seitsemän lukua väliltä 1-40

def lotto():
    while len(numerot) <7:
        luku = random.randint(1,40)
        numerot.add(luku)
    print(numerot)

# kutsutaan funktiota "lotto()"

lotto()