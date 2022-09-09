'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 2 tehtävä 1

    ohjelma kysyy käyttäjän nimen ja tulostaa
    käyttäjän nimen kirjainten määrän
    
'''

# määritetään muuttujat

sukunimi = input("Anna Sukunimesi: ")
pituus = len(sukunimi)

print(f"Nimessäsi on {pituus} merkkiä ")