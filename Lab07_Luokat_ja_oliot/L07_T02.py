'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 7 tehtävä 2

    luodaan Human luokka, jolla on kaksi ominaisuutta: name ja age
    

'''

# luokan määrittely ja luokan ominaisuuksien määrittely

class Human():
    name = ""
    age = ""
    
    def __str__(self):
        return str(self.name) + ", " + str(self.age)

# luodaan Human-oliot ja asetetaan ominaisuudet

Adam = Human()
Adam.name = "Nimi: Adam"
Adam.age = "Ikä: 19"

Eva = Human()
Eva.name = "Nimi: Eva"
Eva.age = "Ikä: 18"


print(Adam)
print(Eva)