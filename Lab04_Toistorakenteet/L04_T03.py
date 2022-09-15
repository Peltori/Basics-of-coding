'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 4 tehtävä 3

    ohjelma kysyy lukuja niin kauan kunnes käyttäjä antaa tyhjän syötteen
    ohjelma laskee kuinka monta lukua käyttäjä antoi
    ja myös lukujen summan

'''

luvut = 0
summa = 0

while True:
    try:
        luku = int(input("Anna kokonaisluku: "))
        luvut += 1
        summa += luku
    except ValueError:
        break

print(f"Lukuja annettu yhteensä: {luvut}")
print(f"Lukujen summa on: {summa}")