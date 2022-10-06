'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 7 tehtävä 4

    luodaan Mobile luokka, jolla on kolme ominaisuutta: "brand" ja "model" ja "price"
    lisätään luokalle konstruktori "init" jonka avulla asetetaan oliolle ominaisuudet

'''

# luokan ja ominaisuuksien luonti

class Mobile():
    brand = ""
    model = ""
    price = ""
    
    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.price) + "€"
    
    def __init__(self, brand = "", model = "", price = 0):
        self.brand = brand
        self.model = model
        self.price = price

phone1 = Mobile("Samsung", "Galaxy", 349)
phone2 = Mobile("Apple", "iPhone 12", 899)

print(phone1)
print(phone2)