fullname = input("What is your name? ")
length = len(fullname)
separator = fullname.find(" ")
firstname = fullname[0:separator]
secondname = fullname[separator+1:length]
print(f" Etunimesi on: {firstname}")
print(f" Sukunimesi on: {secondname}")