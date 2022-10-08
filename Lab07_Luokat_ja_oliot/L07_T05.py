'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 7 tehtävä 5

    luodaan Car luokka, jolla on kolme ominaisuutta: "brand" ja "model" ja "price"
    autotallissa on kolme autoa, luodaan näille omat oliot ja tulostetaan tiedot sekä autojen yhteishinta konsolille

'''

# Car luokan ja ominaisuuksien luonti

class Car():
    brand = ""
    model = ""
    price = ""

    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.price)
    
    def __init__(self, brand = "" , model = "", price = 0):
        self.brand = brand
        self.model = model
        self.price = price

# luodaan Hinta luokka, jonne määritetään __add__() metodi, jonka avulla voidaan laskea objektien arvoja yhteen

class Hinta():

    def __init__(self, summa):
        self.summa = summa

    def __add__(self, summa2):
        return Hinta(self.summa + summa2.summa)

# luodaan Car luokasta auto oliot ja annetaan tiedot olioille

auto1 = Car()
auto1.brand = "Skoda"
auto1.model = "Octavia"
auto1.price = 3000

auto2 = Car()
auto2.brand = "Audi"
auto2.model = "A4"
auto2.price = 4000

auto3 = Car()
auto3.brand = "Volvo"
auto3.model = "V70"
auto3.price = 5000

# luodaan Hinta luokasta hinta olio ja lasketaan hinnat yhteen

hinta1 = Hinta(3000)
hinta2 = Hinta(4000)
hinta3 = Hinta(5000)

kokonaishinta = hinta1 + hinta2 + hinta3

print(f"auto: {auto1}")
print(f"auto: {auto2}")
print(f"auto: {auto3}")
print(f"Autojen hinnat yhteensä: {kokonaishinta.summa}€")