'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 6 tehtävä 1

    funktio tulostaa saadun sekuntiarvon muodossa tunnit:minuutit:sekunnit 

'''

# funktion alustus

def showtime(sekunnit):
    tunnit = sekunnit // 3600
    sekunnit %= 3600
    minuutit = sekunnit // 60
    sekunnit %= 60
    return (f"{tunnit:02d}:{minuutit:02d}:{sekunnit:02d}")

print(showtime(500))
print(showtime(10000))
print(showtime(121000))