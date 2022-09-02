#määritetään muutujat eurot ja sentit ja kysytään käyttäjältä eurojen ja senttien määrää
eurot = int(input("Montako euroa sinulla on? (Anna kokonaisluku) "))
sentit = float(input("Montako senttiä sinulla on? (Anna desimaaleina) "))
summa = eurot + sentit
#tulostetaan muuttujien eurot ja sentit summa
print(f"Rahaa sinulla on {summa:.2f} ")