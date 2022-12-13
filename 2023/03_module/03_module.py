"""
Seznami
"""

"""
Seznam, z VSAJ 3 elementi
printaj CEL seznam v konzolo -> hint: uporabi print()
printaj VSAK element v seznamu v konzolo (v posebej vrstici)

za hitrejse: poglej chat v discordu za ekstra nalogo! hint: Uporabi GOOGLE
"""

print("-- zacetek programa --")

nakupovalni_listek = ["mleko", "jajca", "kruh"]
imena = ["luka", "jan", "peter", "primoz"]
print(nakupovalni_listek)
print(nakupovalni_listek[0])
print(nakupovalni_listek[1])
print(nakupovalni_listek[2])

print(nakupovalni_listek[-1])
print(imena[-2])

seznam = ["kruh"]

"""
Seznami
"""

nakupovalni_listek_dolzina = len(nakupovalni_listek)
print("Dolzina seznama nakupovalni_listek:", nakupovalni_listek_dolzina)

imena_dolzina = len(imena)  # 4
print("Dolzina seznama imena:", len(imena))

print(imena[imena_dolzina - 1])
print(imena[3])

# Motivacija zakaj rabimo len()
nakupovalni_listek = ["mleko", "jajca", "kruh"]
kosarica = []


"""
Naloga za dodajanje elementov

Naredi prazen seznam
"""

ucenci_z_oceno = []
print("Oceno nima noben:", ucenci_z_oceno)
ucenci_z_oceno.append("Luka")  # Append nam doda podano vrednost na konec seznama
ucenci_z_oceno.append("Ana")
ucenci_z_oceno.append("Neza")
ucenci_z_oceno.insert("Marko", 3)
odstranjen_ucenec = ucenci_z_oceno.pop("Neza")

print("Odstranjen ucenec je", odstranjen_ucenec)

ucenci_z_oceno.__contains__()

print(
    "Stevilo ucencev, ki imajo oceno je",
    len(ucenci_z_oceno),
    "in to so:",
    ucenci_z_oceno,
)

"""
Najdi vsaj 3 NOVE funkcije, ki jih lahko klices na seznamu in jih uporabi. 
Prav tako zraven njih napisi v komentarju v 1 stavku, kaj naredijo.
"""


""" BOOLEAN
"""

# >, <, ==, <=, >=

# bool

pravilno = True
nepravilno = False

# and -> kot rezultat pravilno, če sta oba dela enačbe pravilna
# or -> kot rezultat pravilno, če je vsaj en del enačbe pravilen
# not -> obrne vrednost ki jo podamo

operatorIn = pravilno and nepravilno
ali = pravilno or nepravilno
negirano = not nepravilno


# print(operatorIn)
# print(ali)
# print(negirano)
