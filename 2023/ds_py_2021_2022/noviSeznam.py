nakup = []
print("Kaj moraš kupit?")

izdelek = input()

nakup.append(izdelek)

#dajemo na seznam ; ko je vse na seznamu napiši "konec"
while(izdelek != "konec"):
	print("Kaj moraš kupit? (vpisi konec ko si koncal)")
	izdelek = input()
	if(izdelek != "konec" and izdelek not in nakup):
		nakup.append(izdelek)

skupnaCena = 0
#nakupujemo (odstranjujemo iz seznama)
while(len(nakup) != 0): #v oklepaje napiši pogoj
	#tu piši kodo ki hočeš da se ponavlja

	print("Piši 'D' za dodajanje in 'K' za kupovanje")

	nakupAliDodaja = input()
	if(nakupAliDodaja == "D"):
		izdelek = input()
		if(izdelek not in nakup):
			nakup.append(izdelek)
		else:
			print("Izdelek je že na seznamu")

	elif(nakupAliDodaja == "K"):
		odstraniIzdelek = input()
		if(odstraniIzdelek in nakup):
			nakup.remove(odstraniIzdelek)
			print("koliko je izdelek stal?")
			cena = input()
			skupnaCena = skupnaCena + float(cena)
		else:
			print("Izdelka ni seznamu!")
		
	else:
		print("napačna uporaba seznama, piši K ali D")


	print("Na seznamu imaš še: " + str(nakup))
	print("Trenutna cena je " + str(skupnaCena))

print("NAKUP KONČAN :D")
print("ZAPRAVIL/A SI: " + str(skupnaCena) + "!!!!")

#nadaljna koda