'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 2 tehtävä 4
   
    ohjelma laskee käyttäjän iän

'''

# otetaan käyttöön datetime kirjasto
import datetime

# määritellään muuttujat
firstname = input("Anna etunimesi: ")
age_years = int(input("Anna syntymävuotesi: "))
now = datetime.datetime.now()
current_year = now.year

print(f"Hei {firstname}, olet {current_year - age_years} vuotias ")