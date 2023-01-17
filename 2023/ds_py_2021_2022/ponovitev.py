#Program ki izpiše vsa naravna števila od 1 do 20, razen tistih ki so deljiva s 3 ali 5
for i in range(1, 21):
	if(i % 3 != 0 and i % 5 != 0):
		print(i)




#program ki prebere poljubni celi števili in prvega izpiše tolikokrat kot je vrednost drugega 
katero = int(input("Katero stevilo naj izpisem? "))
kolikokrat = int(input("Kolikokrat naj ga izpisem? "))
for i in range(kolikokrat):
	print(katero)





#program, ki prebere poljubno celo število in sestavi novi števili.
#V prvem naj bodo vse sode števke števila in v drugem vse lihe števke v obratnem vrstnem redu.
#Tako iz 1234512436 naredimo števili 31531 in 64242. 
stevilo = input("Soda/Liha\n")
soda = ""
liha = ""
for stevka in stevilo:
	if(int(stevka) % 2 == 0): #Soda
		soda = stevka + soda
	else: #Liha
		liha = stevka + liha
print(soda)
print(liha)


#program, ki bo prebral tromestno naravno število, 
#nato pa iz njega izdelal čimvečje naravno število z enakimi števkami.  Primer: 375 rešitev je  753. 
st = input("Tromestno\n")
st = list(st)
vecjeSt = ""
for i in range(3):
	najvecje = 0
	indexNajvecje = -1
	for stevka in st:
		if int(stevka) > najvecje:
			najvecje = int(stevka)
			indexNajvecje = st.index(stevka)
	vecjeSt += str(najvecje)
	st[indexNajvecje] = "0"
print(vecjeSt)


#Preberi štirimestno pozitivno število in ga izpiši 'obrnjeno'. Tako za število 1234 program izpiše 4321. 

stevilo = input("stirimestno obrnjeno ")
stevilo = list(stevilo)
for i in range(len(stevilo)):
	print(stevilo[len(stevilo) - i])