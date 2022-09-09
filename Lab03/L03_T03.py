'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 3 Tehtävä 3

'''

# muuttujan alustus

luku = int(input("Anna kokonaisluku: "))

if (luku == 10 or luku == 20):
    print("Annettu luku on 10 tai 20: ")

elif (luku == 100 or luku == 200):
    print("Annettu luku on 100 tai 200: ")

else:
    print(f"Annettu luku on: {luku}")