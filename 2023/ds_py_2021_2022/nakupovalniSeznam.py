nakup = ["mleko", "meso", "jabolka", "jajca", "moka", "kruh", "korenje", "mandarine", "radenska", "bomboni"]

rabimoMeso = "meso" in nakup
print(rabimoMeso)
						# če vežemo več booleanov -> and, or, not
while(len(nakup) != 0): # če vežemo več številk -> <, >, ==, !=, <=, >=
	stvar = input()
	moramoKupit = stvar in nakup

	if(moramoKupit == True):
		#pozicija = nakup.index(stvar)
		#nakup[pozicija] = ""
		nakup.remove(stvar)
		print("Kupili smo:" + stvar)
		print(nakup)
	else:
		print("Te stvari ne potrebuješ!")

	print(len(nakup))
