'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 9 tehtävä 2

    ohjelma lukee aikaisemmasta tehtävästä syötetyt nimet tiedostosta ja näyttää ne konsolilla
    tämän jälkeen ohjelma lajittelee nimet aakkosjärjestykseen ja näyttää ne kosolilla uudelleen

'''

# luodaan tyhjä lista

nimet_lista = []

# luetaan tiedostosta nimet
try:
    file = open(r"tekstitiedostot/testi.txt", "r", encoding = "utf-8")

    for nimi in file:
        nimet_lista.append(nimi)

# suljetaan lista

    file.close()

    print(nimet_lista)

# lajitellaan lista aakkosjärjestykseen ja näytetään lista konsolilla

    nimet_lista.sort()
    print(nimet_lista)
    
except:
    print(f"Tiedoston {file} käsittelyssä tapahtui ongelma")
    print("Onko tiedosto varmasti olemassa")