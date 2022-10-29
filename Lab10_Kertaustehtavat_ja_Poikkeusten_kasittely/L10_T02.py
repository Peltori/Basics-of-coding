'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 10 tehtävä 2

    ohjelma kysyy käyttäjän tämän iän, annetun iän perusteella funktio "kerro3()" palauttaa tekstin
    "child" jos ikä on alle 13 vuotta, jos ikä on 13-19 vuotta palautetaan "teen"
    jos ikä on 20-65 vuotta palautetaan "adult", muussa tapauksessa palautetaan "senior"

'''

def kerro3():
    while True:
        try:
            ikä = int(input("Anna ikäsi: "))
        
            if ikä <= 0:
                print("Ikä ei voi olla nolla tai negatiivinen")
                continue
            elif ikä < 13:
                print("child")
            elif ikä >= 13 and ikä < 20:
                print("teen")
            elif ikä >= 20 and ikä < 66:
                print("adult")
            else:
                print("senior")
            break
        
        except ValueError:
            print("Annoitko varmasti pelkän kokonaisluvun?")

kerro3()