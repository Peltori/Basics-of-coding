# määritetään muuttujat fullname, joka kysyy käyttäjän koko nimen
fullname = input("What is your name? ")
# määritetään muuttuja length ja haetaan merkkijonon pituus stringin len() avulla
length = len(fullname)
# määritetään muuttuja separator, ja etsitään stringin find() avulla merkkijonosta välilyönti
separator = fullname.find(" ")
# muuttujista firstname ja secondname voidaan indeksejä käyttämällä määritellä tulostettava teksti
firstname = fullname[0:separator]
secondname = fullname[separator+1:length]
print(f" Etunimesi on: {firstname}")
print(f" Sukunimesi on: {secondname}")