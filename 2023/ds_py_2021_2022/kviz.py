#Naredimo kviz! uporabnik more odgovriti na vsaj 5 uprašanj
#Vsakič ko pravilno odgovrimo na vprašanje, se nam prištejejo točke
#na koncu napiši koliko točk je uporabnik dosegel
#Previlnost odgovora preverjaj v funkciji

#tukaj bojo globalne spremenljivke
tocke = 0


# tukaj se bojo pisale funkcije
def preveriOdgovor(odgovor, pravilenOdgovor):
	#Uporabnik ima 3 poskuse za odgovarjat
	#če odgovori narobe, mu sporočimo da je odgovor napačen in koliko poskusov še ima
	#če odgovori prav pa use isto kot prej
	poskusi = 3
	global tocke

	while poskusi > 0:
		poskusi -= 1
		if(odgovor.lower() == pravilenOdgovor.lower()):
			tocke += 1
			return True
		else:
			if(poskusi == 0):
				return False
			print("Napačen odgovor! Imaš še " + str(poskusi) + " poskusov")
			odgovor = input()
	


#tukaj se bo pisal glavni program	
prviOdg = input("Kaj je glavno mesto avstirje: ")
pravilnostOdgovora = preveriOdgovor(prviOdg, "Dunaj")
if(pravilnostOdgovora == True):
	print("Odgovor je pravilen!!")
	print("Tvoje točke so " + str(tocke))

drugiOdg = input("Kdaj je bil narejen minecraft: ")
pravilnostOdgovora = preveriOdgovor(drugiOdg, "2011")
if(pravilnostOdgovora == True):
	print("Odgovor je pravilen!!")
	print("Tvoje točke so " + str(tocke))

tretjiOdg = input("Najboljsi pripomocek ki ga lahko prineseš v šolo: ")
pravilnostOdgovora = preveriOdgovor(tretjiOdg, "Ravnilo")
if(pravilnostOdgovora == True):
	print("Odgovor je pravilen!!")
	print("Tvoje točke so " + str(tocke))

cetrtiOdg = input("Katera je največja žival: ")
pravilnostOdgovora = preveriOdgovor(cetrtiOdg, "Kit")
if(pravilnostOdgovora == True):
	print("Odgovor je pravilen!!")
	print("Tvoje točke so " + str(tocke))

petiOdg = input("Kaj je smisel življenja, vesolja in vsega nasploh: ")
pravilnostOdgovora = preveriOdgovor(petiOdg, "42")
if(pravilnostOdgovora == True):
	print("Odgovor je pravilen!!")
	print("Tvoje točke so " + str(tocke))

sestiOdg = input("Kaj je najboljša hrana: ")
pravilnostOdgovora = preveriOdgovor(sestiOdg, "Dunajc in pomfri")
if(pravilnostOdgovora == True):
	print("Odgovor je pravilen!!")
	print("Tvoje točke so " + str(tocke))


sedmiOdg = input("Zelo pomembno vprašanje ඞ : ")
pravilnostOdgovora = preveriOdgovor(sedmiOdg, "\n")
if(pravilnostOdgovora == True):
	print("Odgovor je pravilen!!")
	print("Tvoje točke so " + str(tocke))



print("\nDosegel si: " + str(tocke) + " točk")
