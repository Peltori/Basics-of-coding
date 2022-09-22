'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 4 Tehtävä 1

    ohjelma kysyy montako kokonaislukua luodaan
    sen jälkeen kertoo alkion indeksin kymmenellä

'''

# muuttujan alustus

luvut = int(input("Montako lukua luodaan? "))

for luku in range(luvut):
    numbers = 10 * luku
    
    print("luku: " ,numbers)
