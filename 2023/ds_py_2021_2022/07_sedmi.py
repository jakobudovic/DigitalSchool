"""
Program vpraša za oceno na testu, glede na oceno izpiše opis ocene ter pohvalo oziroma spodbudo
"""
print("Kakšno oceno si dobil/a na testu?")

ocena = input()

if(int(ocena) == 1):
	print("Nezadostno!! V prihodnje se več uči >:(")

if(int(ocena) == 2):
	print("Zadostno! Glih za glih, v prihodnje gremo bolj za zihr (zanč)")

if(int(ocena) == 3):
	print("Dobro! V redu ocena ampak lahko narediš bolje!")

if(int(ocena) == 4):
	print("Prav dobro!! Super ocena, le malo manjka do odličnega")

if(int(ocena) == 5):
	print("Odlično!! No končno ena dobra ocena... bravo super si se naučil/a <3")

if(type(ocena) == type("test")):
	print("test1")
	print("test2")

#Naloga rešena še z listom
komentarjiOcen = ["Nezadostno >:(", "Zadostno :(", "Dobro :/", "Prav dobro :)", "Odlično >:)"]

indeksOcene = int(ocena) - 1

komentar = komentarjiOcen[indeksOcene]

print(komentar)

"""
program prejme 2 števili.
če je njuna vsota večja od 500 ju sešteje
če je vsota majnša od 500 ju zmnoži
pol izpiše rezultat

789 567
49 72
249 251
"""

print("Vnesi dve števili")
prvo = int(input())
drugo = int(input())


if(prvo + drugo > 500):
	rezultat = prvo + drugo
	print("Števili se seštejeta v: " + str(rezultat))
else:
	rezultat = prvo * drugo
	print("Števili se zmnožita v: " + str(rezultat))


if(prvo + drugo == 500):
	print("Dej vnesi dve števili k se ne seštejeta u 500 priosm")
