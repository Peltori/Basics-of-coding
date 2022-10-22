'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 9 tehtävä 5

    luodaan funktio "lotto()" joka arpoo lottorivin 7 numeroa väliltä 1-40
    tallentaa ne tiedostoon "lotto.txt" käyttäjältä kysytään montako riviä arvotaan

'''
# otetaan käyttöön "random" kirjasto

import random

# käytetään set tyypin kokoelmaa, koska se ei salli useita samansisältöisiä elementtejä
## tällä eliminoidaan samojen numeroiden mahdollisuus lottorivillä

while True:
    try:
        file = open(r"tekstitiedostot/lotto.txt", "a")
        numerot = set()
        rivit = int(input("Montako riviä arvotaan?"))

        for maara in range(rivit):
            while len(numerot) <7:
                luku = random.randint(1,40)
                numerot.add(luku)
            file.write("Lottorivi = "+ str(numerot) + "\n")

            # tyhjennetään set kokoelma looppien välissä, jotta saadaan puhdas set kokoelma uutta riviä varten
        
            if len(numerot) == 7:
                numerot.clear()
    
        file.close()
        break

    except ValueError:
        print("Annoitko varmasti kokonaisluvun?")

    except:
        print("Tiedoston käsittelyssä tapahtui ongelma")
        print("Onko tiedosto varmasti olemassa?")