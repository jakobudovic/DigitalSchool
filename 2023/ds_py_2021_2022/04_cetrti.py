"""NALOGA:
	Implementiraj naslednje logične operatorje samo z uporabo operatorjev and, or in not:

	implikacija A => B:
	 A/B|true|false
		|----------|
	true|	T |	 F |
		|----------|
	false|	T |	 T |
		-----------

	ekskluzivni ali A xor B:
	 A/B|true|false
		|----------|
	true|	F |	 T |
		|----------|
	false|	T |	 F |
		-----------

	absolutna neresnica N:
	 A/B|true|false
		|----------|
	true|	F |	 F |
		|----------|
	false|	F |	 F |
		-----------

	absolutna resnica P:
	 A/B|true|false
		|----------|
	true|	T |	 T |
		|----------|
	false|	T |	T  |
		-----------
		
"""
A = False
B = True

C = (not A) or B
#print(C)

D = (A and not B) or (not A and B)
#print(D)

E = A or not A #==True

F = B and not B #==False

print("vnesi stevilko")
stevilka = input()
stevilka = int(stevilka) #int(vrednost), float(vrednost)

#nalogica: ali je vneseno število deljivo z 2

deljiva2 = stevilka%2 == 0

print(deljiva2)

#ali je deljiva z 2 in hkrati ni deljiva s 4

deljiva4 = stevilka%4 == 0

rez = deljiva2 and not deljiva4

print(rez)

# vnesemo 2 številki, preverimo ali je prva deljiva z drugo

st1 = input()
st2 = input()

rez2 = st1 % st2 == 0
print(rez2)

