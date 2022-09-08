# määritellään muuttuja pisteet ja tallenetaan muuttujaan käyttäjän antama luku
pisteet = int(input("Anna pisteesi: "))
# määritellään ohjelman logiikka käyttäen ehtolauseita if, elif ja else sekä operaattoria or
if (pisteet == 0 or pisteet == 1):
    print("Arvosanasi on: 0")
elif (pisteet == 2 or pisteet == 3):
    print("Arvosanasi on: 1 ")
elif (pisteet == 4 or pisteet == 5):
    print("Arvosanasi on: 2 ")
elif (pisteet == 6 or pisteet == 7):
    print("Arvosanasi on: 3 ")
elif (pisteet == 8 or pisteet == 9):
    print("Arvosanasi on: 4 ")
elif (pisteet == 10 or pisteet == 11 or pisteet == 12):
    print("Arvosanasi on: 5 ")