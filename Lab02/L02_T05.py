''' määritetään muuttuja firstname ja kysytään käyttäjän etunimi
    määritetään muuttuja length ja haetaan merkkijonon pituus funktion len avulla
    määritetään muuttuja first ja indeksin avulla haetaan merkkijonon ensimmäinen kirjain muuttujasta firstname
'''
firstname = input("Anna etunimesi: ")
length = len(firstname)
first = firstname[0]
#tulostetaan muuttujat firstname ja length sekä kerrotaan muuttuja first ja length keskenään ja tulostetaan muuttujien tulo
print(f"Nimessäsi {firstname} on {length} kirjainta. ")
print(first * length)