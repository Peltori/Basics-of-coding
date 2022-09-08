# määritellään muutujat luku, luku2 ja luku3 tallennetaan käyttäjän antamat luvut näihin muuttujiin
luku = int(input("Anna jokin kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))
# määritellään ohjelman logiikka if, else ja elif ehtolauseilla sekä käytetään and operaattoria
if (luku > luku2 and luku > luku3):
    print(f"Suurempi luku on: {luku}")
elif (luku2 > luku and luku2 > luku3):
    print(f"Suurempi luku on: {luku2}")
else:
    print(f"Suurempi luku on: {luku3}")