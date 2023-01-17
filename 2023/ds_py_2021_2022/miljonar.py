#kviz miljonar z 10 vprašanji
#vsako vprašanje ima 4 možne podane odgovore, od teh je en pravilen
#kviz se rešuje dokler uporabnik ne oddgovori narobe
#uporabnik ima na voljo 2 jokerja, ki mu za dano vprašanje štejeta odgovor kot pravilen
#"joker" -> skip vprašanje in prišteje točko

stJoker = 2

#prostor za funkcije
def preveriOdgovor(odgovor, pravilen):
	global stJoker
	if(odgovor.lower() == pravilen.lower()):
		return True
	elif(odgovor == "joker" and stJoker > 0):
		stJoker -= 1
		return True
	else:
		return False



#prostor za glavno kodo
tocke = 0
vprasanja = ["Kaj je glavno mesto avstrije?\na)ljubljana\nb)dunaj\nc)buddimpešta\nd)maribor", "kaj pije krava?\na)vroča čokolada\nb)mleko\nc)voda\nd)monster", "kaj nam da debela krava?\na)domačo nalogo\nb)marmelada\nc)steak\nd)nevem", "koliko harry potter filmov obstaja?\na)2\nb)7\nc)5\nd)8", "katero od naslednih pesmi je napisal Simon Gregorčič\na)Soči\nb)povodni mož\nc)na golici\nd)gangnam style"]
odgovori = ["b", "c", "a", "d", "a"]

for i in range(len(vprasanja)):
	print("Vprašanje številka " + str(i+1))
	print(vprasanja[i])
	odg = input()
	if(preveriOdgovor(odg, odgovori[i])):
		tocke += 1
	else:
		print("Napačen odgovor! Na kvizu ste dosegli " + str(tocke) + " točk!")
		exit()

print("Bravo! Uspešno ste opravili kviz")

