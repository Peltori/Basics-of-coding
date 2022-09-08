# määritellään muuttuja luku ja tallennetaan käyttähän antama luku muuttujaan
luku = int(input("Anna kokonaisluku: "))
# määritellään ohjelman logiikka if, else ja elif ehtolauseilla sekä käytetään or operaattoria
if (luku == 10 or luku == 20):
    print("Annettu luku on 10 tai 20: ")
elif (luku == 100 or luku == 200):
    print("Annettu luku on 100 tai 200: ")
else:
    print(f"Annettu luku on: {luku}")