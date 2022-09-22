'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 4 Tehtävä 5

    ohjelma kysyy käyttäjän etu ja sukunimen
    tulostaa käyttäjän etunimen ensimmäistä kirjainta
    kirjaimien määrän verran ja tämän jälkeen
    tulostaa sukunimen käänteisessä järjestyksessä

'''

# muuttujien alustus

etunimi = input("Anna etunimesi: ")
sukunimi = input("Anna sukunimesi: ")
pituus = len(etunimi)
pituus2 = len(sukunimi)
eka = etunimi[0]
käänteinen = sukunimi[::-1]
etukirjain = pituus * eka

print(etukirjain, käänteinen)