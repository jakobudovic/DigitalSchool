""" napiši program, ki izpiše vsa števila od 1 do 24 ---> v seznamu brez uporabe while zanke 
--> z uporabo range()""" 

seznam = list(range(1, 25))
print(seznam)


""" napiši program, ki izpiše vsa soda števila od 0 do 100 --> z uporabo range()"""

seznamSodi = list(range(0, 101, 2))
print(seznamSodi)


"""napiši program, ki izpiše vsa liha števila od 1 do 100"""

seznamLihi = list(range(1, 101, 2))
print(seznamLihi)

"""napiši program, ki v konzolo nariše trikotnik iz zvezdic --> z while in dodajanjem znakov besedi"""


visina = input()
visina = int(visina)

stevec = 0
zvezdice = "*"						

while(stevec < visina):
	print(zvezdice)
	stevec += 1
	zvezdice += "*"


"""nariši 6x6 kvadrat iz zvezdic BREZ uprabe zank ---> samo s print"""
print("* * * * * *")
print("* * * * * *")
print("* * * * * *")
print("* * * * * *")
print("* * * * * *")
print("* * * * * *")

print("------------")

for i in range(6):
	print("* * * * * *")
	#print(i)

"""napiši program, ki izpiše pravokotnik, ki je dolg 6 in poljubno visok ---> uporabnik napiše višino"""

print("------------")

visina = input()
visina = int(visina)

for i in range(visina):
	print("* * * * * *")

"""napiši program, ki bo v isti vrstici izpisal poljubno število zvezdic ---> uporabnik pove koliko zvezdic"""
print("-------------")

dolzina = input()
dolzina = int(dolzina) # ----> dolzina = int(input())

zvezdica = ""
for i in range(dolzina):
	zvezdica += "* "
print(zvezdica)

"""Združi to dvoje!! napiši program, ki uporabnika vpraša za višino in širino
in potem nariše pravokotnik iz zvezdic ki ima tako višino in širino"""

print("Koliko bo vrstica dolga?")
dolzina = input()
zvezda = ""
dolzina = int(dolzina)

print("koliko bo vrstica visoka?")
visina = input()
visina = int(visina)

for i in range(dolzina):
	zvezda += " *"

for i in range(visina):
	print(zvezda)

#krajsa resitev
vis = int(input())
dolz = int(input())
for i in range(vis):
	print("* " * dolz)
