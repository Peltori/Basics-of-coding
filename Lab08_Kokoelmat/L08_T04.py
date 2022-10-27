'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 8 tehtävä 4

    tallenetaan kymmenen eri auton tiedot Dictionary kokoelmaan
    autoista tiedetään rekisterinumero ja autonmerkki
    käytetään rekisterinumeroa avaimena
    tulostetaan autot aakkosjärjestyksessä rekisterinumeron mukaan

'''

# luodaan tyhjä dictionary kokoelma autoille
## luodaan myös tyhjä lista avaimille, jotta voidaan lajitella tulostus rekisterinumeron perusteella

autot = {}
keys=[]

dict_autot={
    "BXZ-464" : "Skoda",
    "BXX-423" : "Volvo",
    "ZNF-565" : "Toyota",
    "XDS-222" : "Hyundai",
    "VVV-498" : "Chrysler",
    "CNF-672" : "Mitsubishi",
    "BXZ-565" : "Seat",
    "ULN-888" : "Honda",
    "CFH-123" : "Dodge",
    "ULF-358" : "Volskwagen"
}

for key in dict_autot.keys():
    keys.append(key)

keys.sort()

for key in keys:
    value=dict_autot[key]
    print(key,value)