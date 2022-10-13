'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 8 tehtävä 4

    tallenetaan kymmenen eri auton tiedot Dictionary kokoelmaan
    autoista tiedetään rekisterinumero ja autonmerkki
    käytetään rekisterinumeroa avaimena
    tulostetaan autot aakkosjärjestyksessä rekisterinumeron mukaan

'''

# luodaan Dictionary kokoelma autoille

autot_kokoelma = {
    "Skoda" : {
        "rekisterinumero" : "BXZ-464",
},
    "Volvo" : {
        "rekisterinumero" : "BXX-423",
},
    "Toyota" : {
        "rekisterinumero" : "ZNF-565",
},
    "Hyundai" : {
        "rekisterinumero" : "XDS-222",
},
    "Chrysler" : {
        "rekisterinumero" : "VVV-498",
},
    "Mitsubishi" : {
        "rekisterinumero" : "CNF-672",
},
    "Seat" : {
        "rekisterinumero" : "BXZ-565",
},
    "Honda" : {
        "rekisterinumero" : "ULN-888",
},
    "Dodge" : {
        "rekisterinumero" : "CFH-123",
},
    "Volkswagen" : {
        "rekisterinumero" : "ULF-358",
    }
}

lajiteltu_kokoelma = sorted(autot_kokoelma.items(), key = lambda x: x[1]['rekisterinumero'])

# sorted(autot_kokoelma)

print(lajiteltu_kokoelma)