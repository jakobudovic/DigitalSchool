print("Vnesi svoje ime")
ime = input()

print("Vnesi svoj priimek")
priimek = input()

print("Katerega leta si se rodil?")
leto = input()
leto = int(leto)
starost = 2022 - leto


print("Ali si letos že imel rojstni dan? Da/Ne")
odgovor = input()

if(odgovor == "Ne"):
	starost -= 1 # == starost = starost -1
starost = str(starost)

print("Ime ti je " + ime + " " + priimek + " in star si " + starost + " let")

"""if(leto % 4 == 0):
	if(leto % 100 == 0):
		if(leto % 400 == 0):
			print("Rodil si se na prestopno leto!")
		else:
			print("Nisi se rodil na prestopno leto :(")
	else:
		print("Rodil si se na prestopno leto!")
else:
	print("Nisi se rodil na prestopno leto :(")"""

stiri = leto % 4 == 0
sto = leto % 100 == 0
stiristo = leto % 400 == 0

if((stiri and not sto) or (stiri and sto and stiristo)):
	print("Rodil si se na prestopno leto!")
else:
	print("Nisi se rodil na prestopno leto :(")


"""pogoj = False

if(pogoj):
	print("izvede se if")
else:
	print("izvede se else")

print("zunaj if stavka")"""
