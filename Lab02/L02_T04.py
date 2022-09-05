# määritetään muuttuja firstname ja age_years, kysytään käyttäjän etunimi sekä syntymävuosi
firstname = input("Anna etunimesi: ")
age_years = int(input("Anna syntymävuotesi: "))
# haetaan import määritteellä tämän hetkinen vuosi 
import datetime
# määritetään muuttuja now ja tälle muuttujalle kuluva päivämäärä
now = datetime.datetime.now()
# määritetään muutujalle current_year kuluva vuosi
current_year = now.year
# tulostetaan käyttäjän antama nimi ja vähennetään kuluvasta vuodesta käyttäjän antama syntymävuosi ja tulostetaan erotus
print(f"Hei {firstname}, olet {current_year - age_years} vuotias ")