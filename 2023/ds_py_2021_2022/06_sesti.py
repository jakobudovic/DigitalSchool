seznam = [3, 6, 9, "dvanjast", 15, 18]
print(seznam)

stevilka = seznam[-1]
print(stevilka)

seznam[3] = 12
print(seznam)

seznam.append(21)
print(seznam)
seznam.append(24)
print(seznam)
seznam.append(27)
print(seznam)
seznam.append(30)
print(seznam)

#----------
"""
informacije = []
print("Vnesi ime")
ime = "Tvoje ime je: " + input()
informacije.append(ime)
print("priimek?")
priimek = "Tvoj priimek je: " + input()
informacije.append(priimek)
print("tvoj hobi?")
hobi = "Rad imaš " + input()
informacije.append(hobi)

print(informacije[0])
print(informacije[1])
print(informacije[2])"""


horoskopi = ["kozorog", "vodnar", "ribi", "oven", "bik", "dvojčka", "rak", "lev", "devica","tehtnica","škoripjon", "strelec"]

#naloga: vnesi število, program naj ti pove, kaj si po horoskopu

print("Katerega meseca si se rodil (v stevilkah prosim)")
mesec = int(input())
print("Po horoskopu si: " + horoskopi[mesec-1])

kitajski = ["zmaj", "kaca", "konj", "koza", "opica", "petelin", "pes", "merjasec", "podgana", "bivol", "tiger", "macka"]
#tip zmaj je leto 2000
leto = int(input())

pozicija = leto - 2000
pozicija = pozicija % 12

print("Po kitajskem horoskopu si: " + kitajski[pozicija])


