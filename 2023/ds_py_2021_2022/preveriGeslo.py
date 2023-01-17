import string
#geslo mora biti vsaj dolžine 8 in max 32. Geslo mora imeti vsaj eno veliko črko, malo črko, številko
#in poseben znak

def preveriGeslo(geslo):
	if(len(geslo) > 32 or len(geslo) < 8):
		return False

	jeNotri = [False, False, False, False]
	stNotri = 0
	for crka in geslo:
		if(stNotri == 4):
			break
		if(crka in string.ascii_uppercase):
			if(jeNotri[0] == False):
				stNotri += 1
				jeNotri[0] == True
		elif(crka in string.ascii_lowercase):
			if(jeNotri[1] == False):
				stNotri += 1
				jeNotri[1] == True
		elif(crka in string.punctuation):
			if(jeNotri[2] == False):
				stNotri += 1
				jeNotri[2] == True
		elif(crka in string.digits):
			if(jeNotri[3] == False):
				stNotri += 1
				jeNotri[3] == True

	if(stNotri < 4):
		return False

	return True