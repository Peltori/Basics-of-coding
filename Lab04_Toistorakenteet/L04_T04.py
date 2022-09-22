'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 4 Tehtävä 4

    ohjelma kysyy käyttäjältä luvun väliltä 1-10
    tämän jälkeen näyttää luvut yhdestä annettuun lukuun
    ja luvun neliön

'''

# muuttujien alustus

määrä = 0
neliö = 0
luku = int(input("Anna kokonaisluku väliltä 1-10: "))

for luku in range(luku):
    määrä = luku + 1
    neliö = (luku + 1) ** 2

    print(f"Luvun: {määrä} neliö on: {neliö}")