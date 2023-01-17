"""print("beseda")

range(5)

int() # iz neštevilke dobili številko

input()

str() 

list()"""


def doberDan():
	print("Dober dan!")
	print("Zunaj sije sonce")
	print("Treba bo v šolo")



def kvadratStevila(stevilo):
	kvadrat = stevilo * stevilo
	return kvadrat


# kvadarti cseh stevil od 1 do 100

"""for i in range(1, 101):
	kvadrat = kvadratStevila(i)
	print(kvadrat)"""
	

def trikotnik(velikost, zacetniPresledki):
	for i in range(velikost):
		print(zacetniPresledki * " " + (velikost - i - 1) * " " + (i+1) * "* ")

def obrnjenTrikotnik(velikost, zacetniPresledki):
	for i in range(velikost):
		print(zacetniPresledki * " " + i* " " + (velikost-i)*"* ")



visina = 3
for i in range(visina):
	trikotnik(i+2, (visina -i -1))

print()
obrnjenTrikotnik(3, 0)
print()

for i in range(visina):
	obrnjenTrikotnik(i+2, (visina - i  - 1))
	

#napiši funkcijo, ki poljubnokrat (vnesemo število v funkcijo) ponovi neko besedo (besedo vnesemo v funkcijo)

def ponoviBesedo(kolikokrat, beseda):
	for i in range(kolikokrat):
		print(beseda)


ponoviBesedo(10, "pravi programerji")


