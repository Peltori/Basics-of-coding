'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 5 tehtävä 4

    funktio laskee ja palauttaa automatkaan kuluneen
    polttoaineen määrän yhden desimaalin tarkkuudella

'''

# funktion alustus

def get_fuel(km, keskikulutus):
    litrat = ((km * keskikulutus) / 100)
    return (f"Polttoainetta kulunut {litrat:.1f} ltr")

print(get_fuel(100, 7.5))
print(get_fuel(220, 6.9))