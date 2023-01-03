# print("Kakšno oceno si dobil/a na testu?")
# ocena = input()

"""
0.
Ponovitev if

Napisi program, ki te vprasa, koliko si dobil oceno na testu matematike,
izpise pa ti ali moras test pisati se enkrat ali ne.

Izpis/-a naj bosta smiselna.
"""

ocena = int(input("Koliko si pisal matematiko? "))
if ocena > 1:  # vsaj dve (2, 3, 4, 5)
    print("Ne rabis ponavljat.")
else:  # (1)
    print("Rabis ponovno pisat matematiko.")

# (2, 3, 4, 5) + (1) = (1, 2, 3, 4, 5)

"""
1.
program prejme 2 števili.
če je njuna vsota večja ali enaka od 500 ju sešteje
če je vsota manjša od 500 ju zmnoži
Potem izpiše rezultat.

789 567 = 1356
49 72 = 3528
249 251 = 500
"""

# Sprejmi stevila in shrani kot int
st1 = int(input("Vnesi stevilo 1: "))
st2 = int(input("Vnesi stevilo 2: "))

# Sestej stevili in si shrani njuno vsoto
vsota = st1 + st2
if vsota >= 500:
    print(vsota)
else:
    print(st1 * st2)


"""
2.a
Napisi program, ali dopolni prvi program, ki ti izpise z besedo, kaksno oceno si dobil
na podlagi uporabnikovega stevilcnega vnosa.

(Temu primerno ga na zacetku vprasaj, koliksno oceno je dobil.)
"""


"""
2.b
Prejsnji program z ocenami dopolni (kopiraj v novo datoteko in dopolni), naredi s pomocjo seznamov. 
Namig 1: Ali sploh potrebujes pogojne stavke?
Namig 2: Oceno lahko uporabis kot indeks za dostopanje elementov v seznamu.
"""

"""
3.
Naredi program, ki otroke razdeli v 4 skupine. 
Skupina A: Fantje do 12. leta.
Skupina B: Punce do 12. leta.
Skupina C: Fantje od vkljucno 12. leta.
Skupina D: Punce od vkljucno 12. leta.

Temu primerno uporabnik vnese svoj spol in starost, program pa mu izpise v katero skupino pripada.

Primer delovanja programa:
Koliko si star? 13
Ali si fant ali punca (m/f)? m
Si fant, star 13 let, zato spadas v skupino C.
"""
