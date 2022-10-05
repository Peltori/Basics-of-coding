'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 5 tehtävä 4

    funktio laskee ja palauttaa automatkaan kuluneen
    polttoaine kustannuksen 2 desimaalin tarkkuudella

'''

# funktion alustus

def get_cost(km, keskikulutus, litrahinta):
    kustannus = ((km * keskikulutus) / 100 * litrahinta)
    return (f"kustannus {kustannus:.2f} €")

print(get_cost(100, 7.5, 1.88))
print(get_cost(220, 6.9, 1.88))