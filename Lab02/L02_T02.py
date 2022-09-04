#määritetään muuttujat etunimi ja sukunimi, kysytään käyttäjältä etu- ja sukunimi
etunimi = input("Anna etunimesi: ")
sukunimi = input("Anna sukunimesi: ")
#upper() avulla saadaan muutettua pienet kirjaimet isoiksi merkkijonossa
#määritetään muuttujat a ja b ja annetaan näille muuttujat etunimi ja sukunimi
a = etunimi.upper()
b = sukunimi.upper()
#tulostetaan muuttujat a ja b
print(a, b)