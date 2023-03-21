"""
KVIZ
Napisite funkcijo, ki preveri, ali je uporabnikov odgovor na vprasanje pravilen.
Napisite program, ki bo vprasal uporabnika vsaj 5 razlicnih vprasanj, on pa mora nanje odgovoriti. 
Z napisano funkcijo preverite, ali je njegov odgovor pravilen ali ne.
Tekom programa si zapomni stevilo pravilno odgovorjenih vprasanj.
Na koncu izpisi stevilo nabranih tock aka stevilo pravilno odgovorjenih vprasanj.


Primer:
def preveri_odgovor(ugib, odgovor, tocke):
    # TODO
    return tocke 

print("Ugibaj glavna mesta!")
ugib = input("Ugani glavno mesto Hrvaske: ")
preveri_odgovor(ugib, "Zagreb", tocke)

1. Ce je vprasanje, ali zna delfin plavati in uporabnik odgovori z DA ali Da,
ali bo v obeh primerih dobil tocke?
2. Now let's make this program more interesting by allowing 
the users to guess three (3) times in one question.
"""

tocke = 0


def preveri_odgovor(ugib, odgovor, tocke):
    if ugib.lower() == odgovor.lower():
        tocke = tocke + 1
        print(f"Odgovor je pravilen!")
    else:
        # Ne povecas
        print(f"Odgovor je napacen :(")
    return tocke


print("Ugibaj glavna mesta!")
ugib = input("Ugani glavno mesto Hrvaske: ")
tocke = preveri_odgovor(ugib, "Zagreb", tocke)  # shrani novo vrednost tock !!

ugib = input("Ugani glavno mesto Slovenije: ")
tocke = preveri_odgovor(ugib, "Ljubljana", tocke)  # shrani novo vrednost tock !!


print(f"total points: {tocke}")
