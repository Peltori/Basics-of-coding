'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 9 tehtävä 5

    ohjelma kysyy käyttäjältä montako riviä luodaan
    sen jälkeen arpoo lotto rivejä käyttäjän syötteen mukaisesti numeroiden 1-40 välillä
    lajittelee rivissä olevat numerot pienimmästä suurimpaan
    ja tallentaa ne tiedostoon "lotto.txt"

'''
# otetaan käyttöön "random" kirjasto

import random

# käytetään set tyypin kokoelmaa, koska se ei salli useita samansisältöisiä elementtejä
## tällä eliminoidaan samojen numeroiden mahdollisuus lottorivillä

while True:
    try:
        file = open(r"tekstitiedostot/lotto.txt", "a")
        set_numerot = set()
        lst_numerot = []
        rivit = int(input("Montako riviä arvotaan? "))
        
        # tarkistetaan antaako käyttäjä positiivisen kokonaisluvun

        if rivit <= 0:
            print("Annoitko positiivisen luvun?")
            continue
        
        for maara in range(rivit):
            while len(set_numerot) <7:
                luku = random.randint(1,40)
                set_numerot.add(luku)

            # tyhjennetään "lst_numerot" sekä "set_numerot" jotta saadaan puhtaat kokoelmat uutta riviä varten
            ## listojen tyhjentämisen jälkeen kirjoitetaan rivi tiedostoon "lotto.txt"
        
            if len(set_numerot) == 7:
                lst_numerot.extend(set_numerot)
                lst_numerot.sort()
                file.write("Lottorivi = "+ str(lst_numerot) + "\n")
                set_numerot.clear()
                lst_numerot.clear()
        
        # suljetaan lopuksi tiedosto

        file.close()
        print("Rivit tallennetu tiedostoon lotto.txt, lopetetaan ohjelma")
        break
    
    except ValueError:
        print("Annoitko varmasti kokonaisluvun?")

    except:
        print("Tiedoston käsittelyssä tapahtui ongelma")
        print("Onko tiedosto varmasti olemassa?")