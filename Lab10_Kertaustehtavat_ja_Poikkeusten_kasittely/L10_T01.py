'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 10 tehtävä 1

    ohjelma tulostaa konsoliin pankkitilin saldon (alkusaldo 2000€) ja kysyy kuinka monta euroa ja senttiä talletetaan tilille
    kysymysten jälkeen tulostetaan saldo konsoliin

'''

# alustetaan muuttuja saldo

saldo = 2000

print(f"Bank account balance: {saldo} €")

eurot = int(input("How many euros will be added to the balance? "))
sentit = int(input("How many cents will be added to the balance? "))

saldo += eurot + (sentit / 100)

print(f"Bank account balance: {saldo} €")