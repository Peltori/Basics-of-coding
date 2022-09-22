'''
    author: petri peltomaa
    ohjelmoinnin perusteet: Labra 5 Tehtävä 2

    Luodaan funktio, jolle viedään 2 parametria.
    Funktio palauttaa annettujen parametrien erotuksen

'''


def subtract(num, num2):
    return (num - num2)
print(subtract(4, 2))


'''

Sama ohjelma, mutta käyttäjän antaman inputin mukaan.

num = int(input("Anna kokonaisluku: "))
num2 = int(input("Anna toinen kokonaisluku: "))

def subtract(num, num2):
    return (num - num2)
print(subtract(num, num2))

'''