# määritellään muutujat luku ja luku2, tallennetaan käyttäjän antamat luvut näihin muuttujiin
luku = int(input("Anna jokin kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
# määritellään ohjelman logiikka if ja else ehtolauseilla
if luku < luku2:
    print(f"Pienempi luku on: {luku}")
else:
    print(f"Pienempi luku on: {luku2}")