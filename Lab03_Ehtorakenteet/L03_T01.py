'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 3 Tehtävä 1
    
    ohjelma kysyy käyttäjältä 2 kokonaislukua
    ohjelma tulostaa annteusta luvuista pienemmän

'''

# alustetaan muuttujat

luku = int(input("Anna jokin kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))

if luku < luku2:
    print(f"Pienempi luku on: {luku}")

else:
    print(f"Pienempi luku on: {luku2}")