'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 1 tehtävä 4
    
    ohjelma laskee käyttäjän antamien lukujen
    summan, erotuksen ja tulon
    
'''

luku = int(input("Anna kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku "))
summa = luku + luku2
erotus = luku - luku2
tulo = luku * luku2

print(f"Lukujen {luku} ja {luku2} summa on: ", summa)
print(f"Lukujen {luku} ja {luku2} erotus on: ", erotus)
print(f"Lukujen {luku} ja {luku2} tulo on: ", tulo)