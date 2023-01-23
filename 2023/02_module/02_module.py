# 2 + x = 4
# x -> je spremenljivka

# Spremenljivka / variable.

"""
x = 2  # assignment, dodelitev
print(x)

mark_age = 12

ucenec1 = "Mark"
ucenec2 = "Maks"

name = "Uros"
surname = "Udovic"
print("Moje prvo ime je", name, "priimek pa", surname)
"""


"""
Koliko denarja imamo na voljo cez dan za hrano, 
ce razpolagamo s 30 evri, 5 dni.
"""
denar = 30
dni = 5
denar_za_hrano_na_dan = denar / dni
print(denar_za_hrano_na_dan)

"""
Miha ima 52 eur na dan žepnine, na poti v šolo mu ukradejo 8 eur
hrana stane 5 eurou
Koliko obrokov si lahko miha na dan privošči?
Format odgovora: "Miha si lahko na dan privosci X obrokov."

Koliko denarja mu na koncu dveva ostane, ce si kupi vse mozne obroke?
"""

denar = 52
ukradejo = 8
hrana = 5

# Koliko obrokov si lahko miha na dan privošči?
ostanek_denarja = denar - ukradejo  # 44
stevilo_obrokov = ostanek_denarja // hrana  # 8
# stevilo_obrokov = int(ostanek_denarja / hrana)  # 8
print("Miha si lahko na dan privosci", stevilo_obrokov, "obrokov.")

ostanek_za_sladico = ostanek_denarja - (hrana * stevilo_obrokov)  # 4
print("Za sladico Mihatu ostane", ostanek_za_sladico, "evre.")


"""
Primeri tipov spremenljivk
"""
starost = 18  # int
teza = 90.5  # float
ime = "Jakob"  # string
nakupovalni_listek = ["mleko", "jajca", "kruh"]  # list
stopnicke = {"drugi": "Hana", "prvi": "Luka", "tretji": "Metod"}  # dict (slovar)
obdobja_v_zgodovini = ("prazgodovina", "stari vek", "srednji vek", "novi vek")  # tuple


"""
Seznami
"""
nakupovalni_listek = ["mleko", "jajca", "kruh"]
print(nakupovalni_listek)



print(nakupovalni_listek[0])  # dostopanje do PRVEGA elementa
print(nakupovalni_listek)

seznam = ["kruh"]

"""
Seznam, z VSAJ 3 elementi
printaj CEL seznam v konzolo -> hint: uporabi print()
printaj VSAK element v seznamu v konzolo (v posebej vrstici)

za hitrejse: poglej chat v discordu za ekstra nalogo! hint: Uporabi GOOGLE
"""

# OK
print(nakupovalni_listek)
print("Konec programa!")
