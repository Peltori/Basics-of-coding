'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 2 tehtävä 5
    
    ohjelma kysyy käyttäjältä etunimen ja
    ohjelma tulostaa konsoliin nimen kirjainten määrän sekä
    nimen ensimmäistä kirjainta nimen kirjainten määrän verran

'''

# määritetään muuttujat

firstname = input("Anna etunimesi: ")
length = len(firstname)
first = firstname[0]

print(f"Nimessäsi {firstname} on {length} kirjainta. ")
print(first * length)