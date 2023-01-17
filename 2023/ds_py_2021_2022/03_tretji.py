"""
miha 52 eur na dan žepnine, na poti v šolo mu ukradejo 8 eur
hrana stane 5 eurou
koliko obrokov si lahko miha na dan privošči
koliko denarja mu na koncu dveva ostane
miha si lahko najame stražarja, stražarja si lahko najame samo, ce mu ostane 5 eur.
ali si lahko najame stražarja.
stražar ma rd bogate otroke, tako da bo naredil izjemo, če otrok nima dovolj denarja
ampak dobi več kot 50 eur žepnine
"""

kesh = 52
kraja = 8
hrana = 5

#ukradejo nam denar
poKraji = kesh - kraja

+ - * / (6 + 5) * 2
%

5/2 = 2.5
5%2 = 1

5 == 3 --> False
5 == 5 --> True

False and True

#to je komentar

obroki = int(poKraji / hrana)

ostanek = poKraji % hrana

# bool naloga
stražar = 5

aliS = ostanek >= 5

smoBogati = kesh > 50

izjema = smoBogati and not aliS

print(aliS)
print(izjema)


#print(obroki)
#print(ostanek)

"""to je dolg komentar,
pišemo ga lahko tudi čez več vrstic"""

#print(kesh < hrana)

# >, <, ==, <=, >=

#bool

pravilno = True
nepravilno = False

# and -> kot rezultat pravilno, če sta oba dela enačbe pravilna
# or -> kot rezultat pravilno, če je vsaj en del enačbe pravilen
# not -> obrne vrednost ki jo podamo

operatorIn = pravilno and nepravilno
ali = pravilno or nepravilno
negirano = not nepravilno


#print(operatorIn)
#print(ali)
#print(negirano)


