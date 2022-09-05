# määritetään muuttujat etunimi ja sukunimi, jotka kysyvät käyttäjän etu- ja sukunimen
etunimi = input("Anna etunimesi: ")
sukunimi = input("Anna sukunimesi: ")
# upper() avulla saadaan muutettua pienet kirjaimet isoiksi merkkijonossa
a = etunimi.upper()
b = sukunimi.upper()
# tulostetaan muuttujat a ja b
print(a, b)