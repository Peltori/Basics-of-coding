'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 2 tehtävä 2
    ohjelma tulostaa käyttäjän antaman nimen isolla

'''

# määritetään muuttujat

etunimi = input("Anna etunimesi: ")
sukunimi = input("Anna sukunimesi: ")
etunimi_iso = etunimi.upper()
sukunimi_iso = sukunimi.upper()

print(etunimi_iso, sukunimi_iso)