'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 7 tehtävä 3

    luodaan Cat luokka, jolla on kaksi ominaisuutta: "name" ja "color", sekä metodi "miau"
    luodaan luokasta Cat kaksi erilaista kissa-oliota, kissa oliot myös naukuvat

'''

# luokan ja ominaisuuksien määrittely

class Cat():
    name = ""
    color = ""
    
    def __str__(self):
        return self.name + ", " + self.color
    
    def miau(self):
        return f"{self.name} says: Meoooooooooow!"

# luodaan kissa-oliot ja asetetaan ominaisuudet

Kit = Cat()
Kit.name = "Kit"
Kit.color = "color: black"

Kat = Cat()
Kat.name = "Kat"
Kat.color = "color: white"


print(Kit)
print(Kat)
print(Kit.miau())
print(Kat.miau())