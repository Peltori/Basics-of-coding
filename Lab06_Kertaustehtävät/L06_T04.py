'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 6 tehtävä 4

    ohjelma kysyy arvostelupisteet yhdelle hypylle ja tulostaa
    tyylipisteiden summan vähennettynä pienin ja suurin luku tästä summasta
    
'''

# muuttujien alustusta

pisteet_lista = []
hypyt = 0
pisteet = 0

# while looppi lisää annetut numerot listaan, josta haetaan funktioiden min() ja max() avulla suurin ja pienin luku ja vähennetään ne kokonaispisteistä

while True:
    hyppy = int(input("Anna hypyn tyylipisteet välillä 1-20 kiitos: "))
    pisteet_lista.append(hyppy)
    pisteet += hyppy
    hypyt += 1
    if hypyt == 5:
        pienin = min(pisteet_lista)
        suurin = max(pisteet_lista)
        kokonaispisteet = pisteet - suurin - pienin
        break
    else:
        continue

print(kokonaispisteet)