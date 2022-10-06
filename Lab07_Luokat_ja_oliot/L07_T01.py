'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 7 tehtävä 1

    luodaan Pelikortti luokka, jolla on kaksi ominaisuutta: maa ja arvo
    luodaan myös 5 Pelikortti-oliota 

'''

# luokan määrittely ja luokan ominaisuuksien määrittely

class Pelikortti():
    maa = ""
    arvo = 0

# luodaan pelikortti-oliot ja asetetaan ominaisuudet

kortti1 = Pelikortti()
kortti1.maa = "Pata"
kortti1.arvo = "2"

kortti2 = Pelikortti()
kortti2.maa = "Hertta"
kortti2.arvo = "14"

kortti3 = Pelikortti()
kortti3.maa = "Risti"
kortti3.arvo = "10"

kortti4 = Pelikortti()
kortti4.maa = "Ruutu"
kortti4.arvo = "8"

kortti5 = Pelikortti()
kortti5.maa = "Pata"
kortti5.arvo = "13"

print(kortti1.maa , kortti1.arvo)
print(kortti2.maa , kortti2.arvo)
print(kortti3.maa , kortti3.arvo)
print(kortti4.maa , kortti4.arvo)
print(kortti5.maa , kortti5.arvo)