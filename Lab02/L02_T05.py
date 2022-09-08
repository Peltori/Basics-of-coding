'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 2 tehtävä 5

'''

# määritetään muuttujat
firstname = input("Anna etunimesi: ")
length = len(firstname)
first = firstname[0]

print(f"Nimessäsi {firstname} on {length} kirjainta. ")
print(first * length)