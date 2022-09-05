''' määritetään muuttuja firstname ja age_years, kysytään käyttäjän etunimi sekä syntymävuosi
    haetaan import määritteellä tämän hetkinen vuosi
    määritetään muuttuja now ja tälle muuttujalle kuluva päivämäärä 
    määritetään muutujalle current_year kuluva vuosi
'''
firstname = input("Anna etunimesi: ")
age_years = int(input("Anna syntymävuotesi: "))
import datetime
now = datetime.datetime.now()
current_year = now.year
# tulostetaan käyttäjän antama nimi ja vähennetään kuluvasta vuodesta käyttäjän antama syntymävuosi ja tulostetaan erotus
print(f"Hei {firstname}, olet {current_year - age_years} vuotias ")