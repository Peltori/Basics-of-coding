# määritetään muuttujat fullname, joka kysyy käyttäjän koko nimen
fullname = input("What is your name? ")
# määritetään muuttuja length ja haetaan merkkijonon pituus stringin len() avulla
'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 2 tehtävä 3
    
'''

# määritetään muuttujat
length = len(fullname)
separator = fullname.find(" ")
firstname = fullname[0:separator]
secondname = fullname[separator+1:length]

print(f" Etunimesi on: {firstname}")
print(f" Sukunimesi on: {secondname}")