# Ohjelmoinnin perusteet harjoitustyö

Toteutus TTC2030-3032

## "Linux-ässä tietovisa" Linuxin historiasta/käyttöjärjestelmästä

## Alkuvalmistelut

Asenna git.<br />
Asenna python 3.10 tai 3.11 versio Microsoft Storesta tai pythonin sivuilta.<br />
Voit myös asentaa Visual Studio Coden halutessasi.<br />

[Visual Studio Code lataus](https://code.visualstudio.com/)<br />
[Pythonin lataus](https://www.python.org/downloads/)<br />
[git lataus](https://git-scm.com/)

## Repon kloonaus ja ohjelman käynnistys

Ohjelman ajaminen on testattu Windowsilla Visual Studio Codella sekä Windowsin terminaalilla, python 3.10 versiolla sekä 3.11 versiolla.

Cloonaa repo haluamaasi kansioon muualle kuin "C:" aseman juureen Windowsissa tai root "/" hakemistoon Linuxilla.<br />
Aja ohjelma "Tietovisa.py" "ttc2030" kansion sisällä.<br />
Ohjelman ajamiseen ei tarvitse asennella mitään pythonin lisäosia.<br />
Voit myös ajaa ohjelman Visual Studio Coden avulla.<br />
"Pisteet" kansio pitää löytyä "Harjoitustyö" kansion juuresta, muuten ohjelma ei toimi.<br />
Älä suorita pythonia "Harjoitustyö" kansiosta vaan ttc2030 kansion juuresta seuraavasti.


```
git clone https://gitlab.labranet.jamk.fi/AC7995/ttc2030.git
cd .\ttc2030\
python ".\Harjoitustyö\Tietovisa.py"
```

## Visan toiminta/käyttöohjeet

Ohjelman suoritus alkaa ja ohjelma kysyy ensin pelaajan nimen.<br />
Tämän jälkeen kysymykset tulostetaan yksi kerrallaan vastausvaihtoehtojen kanssa.<br />
Vastaa kysymyksiin numeroilla 0, 1 tai 2.<br />
Kysymyksiä kysytään 5 kappaletta jonka jälkeen ohjelma sammuu.<br />
Näet oikeiden vastausten määrän "Harjoitustyö/Pisteet/Visailun_pisteet.txt" hakemistosta.<br />
Komentoihin liittyvät kysymykset on testattu Linuxilla bash shellillä.

# Miksi ajaisit ohjelmani?

Tykkäät visailuista tai muuten vain haluat testata taitojasi Linux tietämyksestäsi.<br />
Ohjelma on kevyt ja toimii nopeasti eikä vie kovalevytilaa juurikaan.<br />

# Tekijä/opsikelijatunnus

Petri Peltomaa/AC7995

# Sähköposti

AC7995@student.jamk.fi