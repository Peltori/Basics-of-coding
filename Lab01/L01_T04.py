# määritetään muuttujat luku ja luku2 ja kysytään käyttäjältä kaksi kokonaislukua
luku = int(input("Anna kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku "))
# määritetään muuttujat ja laskutoimitukset
summa = luku + luku2
summa2 = luku - luku2
summa3 = luku * luku2
# tulostetaan lukujen summa, erotus ja tulo
print(f"Lukujen {luku} ja {luku2} summa on: ", summa)
print(f"Lukujen {luku} ja {luku2} erotus on: ", summa2)
print(f"Lukujen {luku} ja {luku2} tulo on: ", summa3)