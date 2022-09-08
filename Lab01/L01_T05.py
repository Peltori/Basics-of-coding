'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 1 tehtävä 5
    
'''

eurot = int(input("Montako euroa sinulla on? (Anna kokonaisluku) "))
sentit = float(input("Montako senttiä sinulla on? (Anna desimaaleina) "))
summa = eurot + sentit

print(f"Rahaa sinulla on {summa:.2f} ")