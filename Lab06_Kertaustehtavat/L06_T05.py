'''
    author: Petri Peltomaa
    ohjelmoinnin perusteet: Labra 6 tehtävä 5

    ohjelman funktio show_cm() muuntaa parametrina annetun senttimetri arvon tuumiksi
 
'''

def show_cm(inch):
    cm = inch * 2.54
    return (f"{inch} tuumaa on {cm} cm")

print(show_cm(2))
print(show_cm(4.5))
print(show_cm(12))