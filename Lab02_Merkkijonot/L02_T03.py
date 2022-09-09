'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 2 tehtävä 3
    ohjelma tulostaa käyttäjän etunimen ja sukunimen välilyönnin perusteella
    
'''
# määritetään muuttujat

fullname = input("What is your name? ")
length = len(fullname)
separator = fullname.find(" ")
firstname = fullname[0:separator]
secondname = fullname[separator+1:length]

print(f" Etunimesi on: {firstname}")
print(f" Sukunimesi on: {secondname}")