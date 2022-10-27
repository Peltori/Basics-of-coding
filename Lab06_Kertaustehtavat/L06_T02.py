'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 6 tehtävä 2

    funktio "celToFah()" muutta celsius-asteet fahrenheiteiksi
    funktio "fahToCel()" muuttaa fahrenheit-asteet celsius asteiksi 

'''

# celsiuksista fahrenheiteiksi 

def celToFah(celsius):
    fahrenheit = celsius * 1.8 + 32
    return (f"{fahrenheit:.1f}")

# fahrenheiteista celsiuksiksi

def fahToCel(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return (f"{celsius:.1f}")

print(celToFah(10.0))
print(fahToCel(38.0))