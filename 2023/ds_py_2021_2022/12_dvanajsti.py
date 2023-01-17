import math
import random
import preveriFunkcija as pf
import string
import preveriGeslo as preveri

"""
stevilo = 25
koren = math.sqrt(stevilo)
print(koren)

preveriFunkcija.reciZivjo()
"""

#listZnakov = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "z", "x", "y", "w", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


#dolzina = int(input("Kako dolgo geslo hočeš?: "))
while(True):
	dolzina = random.randint(8, 28)
	geslo = ""
	zeVBesedi = [False, False, False, False]
	for i in range(dolzina):
		izbira = random.choice([0, 1, 2, 3])

		
		if(i + 3 >= dolzina):
			vsiSoZeNotri = True
			for prisotnost in zeVBesedi:
				if(prisotnost == False):
					vsiSoZeNotri = False
			if(vsiSoZeNotri == False):
				while(zeVBesedi[izbira]):
					izbira += 1 
					izbira = izbira % 4

		if(izbira == 0):#Velike črke
			znak = random.choice(string.ascii_uppercase)
		elif(izbira == 1):#Male črke
			znak = random.choice(string.ascii_lowercase)
		elif(izbira == 2):#Posebni znaki
			znak = random.choice(string.punctuation)
		elif(izbira == 3):#Številke
			znak = random.choice(string.digits)

		zeVBesedi[izbira] = True
		geslo += znak

	print("Tvoje novo geslo je:\n" + geslo)
	seEnkrat = input("Ali hoces novo geslo? (y/n): ")
	if(seEnkrat == "n"):
		break

print("Tvoje geslo je:\n" + geslo)
print(preveri.preveriGeslo(geslo))
#Upgrade!! geslo mora biti vsaj dolžine 8 in max 32. Geslo mora imeti vsaj eno veliko črko, malo črko, številko
#in poseben znak -> DONE!
