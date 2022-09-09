'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 3 Tehtävä 2
    
    ohjelma kysyy käyttäjältä 3 lukua   
    ohjelma tulostaa annetuista luvuista suurimman luvun

'''

# muuttujien alustus

luku = int(input("Anna jokin kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

if (luku > luku2 and luku > luku3):
    print(f"Suurempi luku on: {luku}")

elif (luku2 > luku and luku2 > luku3):
    print(f"Suurempi luku on: {luku2}")

else:
    print(f"Suurempi luku on: {luku3}")