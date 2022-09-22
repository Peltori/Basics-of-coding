'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 5 tehtävä 3

    funktio palauttaa annettujen parametrien
    keskiarvon yhden desimaalin tarkkuudella

'''

# funktion alustus

def average(num, num2, num3):
    keskiarvo = ((num + num2 + num3) / 3)
    return (f"{keskiarvo:.1f}")

print(average(2, 4, 6))
print(average(5, 5, 6))
