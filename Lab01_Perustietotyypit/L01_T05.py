'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 1 tehtävä 5

    ohjelma kysyy käyttäjän rahamäärän
    ohjelma laskee luvut yhteen ja tulostaa summan konsoliin
    
'''

eurot = int(input("Montako euroa sinulla on? "))
sentit = int(input("Montako senttiä sinulla on? "))
summa = eurot + (sentit * 0.01)

print(f"Rahaa sinulla on {summa} ")