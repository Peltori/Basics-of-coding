'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 3 Tehtävä 5
    
    Kysy käyttäjältä 5 lukua
    Laske yhteen ne luvut jotka ovat nollaa suurempia 

'''

# alustetaan muuttujat ja laskuri

num = int(input("Anna luku: "))
num2 = int(input("Anna toinen luku: "))
num3 = int(input("Anna kolmas luku: "))
num4 = int(input("Anna neljäs luku: "))
num5 = int(input("Anna viides luku: "))
numbers = num, num2, num3, num4, num5
value = 0

# looppi tarkastaa onko luku nollaa suurempi

for number in numbers:
    if number > 0:
        value += number

print(value)