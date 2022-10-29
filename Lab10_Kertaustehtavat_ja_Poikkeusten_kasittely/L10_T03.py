'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 10 tehtävä 3

    ohjelma kysyy käyttäjää antamaan vuosiluvun ja tämän järkeen kertoo onko annettu vuosi karkausvuosi

'''


while True:
    try:
        vuosi = int(input("Anna vuosi "))
        
        if vuosi % 4 == 0 and vuosi % 100 == 0 and vuosi % 400 == 0:
            print(f"Year {vuosi} is a leap year")
        elif vuosi % 4 == 0 and vuosi % 100 != 0:
            print(f"Year {vuosi} is a leap year")
        elif vuosi % 400 == 0:
            print(f"Year {vuosi} is a leap year")
        else:
            print(f"Year {vuosi} is not a leap year")
        break
    
    except ValueError:
        print("Did you give an integer?")