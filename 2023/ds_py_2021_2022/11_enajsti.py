#Funkcija, ki na naš seznam doda vse stvari na drugem seznamu -> torej funkcija ki združi seznama

glavniSeznam = []

def zdruziSeznama(prviSeznam, drugiSeznam):
	for element in prviSeznam: 
		if(element not in drugiSeznam):
			drugiSeznam.append(element)

"""def testFunkcija(stevilo):
	stevilo += 5
	print(stevilo)"""

seznam1 = ["jabolko", "hruška", 42, False]
seznam2 = ["marelica", "jabolko", 35, 12, False]
print(seznam2)
zdruziSeznama(seznam1, seznam2)
print(seznam2)


"""testStevilo = 7
testFunkcija(testStevilo)
print(testStevilo)"""


# Napiši funkcijo, ki sprejme dva seznama, in iz prvega seznama odstrani vse elemente, ki so v drugem seznamu
seznamOdstrani = [42, False, True, 15, "ananas", "marelica"]

def odstraniIzSeznama(originalniSeznam, odstrani):
	for element in odstrani:
		if(element in originalniSeznam):
			originalniSeznam.remove(element)

odstraniIzSeznama(seznam2, seznamOdstrani)
print(seznam2)


# Napiši funkcijo ki prejme višino in nariše kvadrat
def kvadrat(visina):
	for i in range(visina):
		print(visina * "* ")

# Napiši funkcijo ki prejme višino in širino ter nariše pravokotnik
def pravokotnik(visina, sirina):
	for i in range(visina):
		print(sirina * "* ")

print()
kvadrat(4)
print()
pravokotnik(6, 9)
