# definicija funkcije
def pozdrav(ime, msg):  # parameter
    print(f"Zvijo ucenec {ime}! {msg}")


# klic funkcije
# pozdrav("Klemen", "Ali si naredil 7. nalogo?")  # argument
# pozdrav("Peter", "Vse najboljse za rd!")  # argument
# pozdrav("Luka", "")
# pozdrav("", "Kako si danes?")


def sestej_stevilia(a, b):
    vsota = a + b
    return vsota


odgovor = sestej_stevilia(10, 5)  # 15
print(odgovor)


"""
A parameter is the variable listed inside the parentheses in the function definition.
An argument is a value that is sent to the function when it is called.
"""


def blok_kode(ime, priimek, starost):
    print(f"Zivjo, {ime}, {starost}")
    print(f"Danes je 21. feb. 2023")
    print(f"Ucili se bomo funkcije.")


def sprintaj_ime_nkrat(ime, n):
    for i in range(n):
        print(f"{ime}")


# sprintaj_ime_nkrat("jakob", 5)


def razcleni_imena(imena):  # ["ajk", "andraz", "erik", "jan", "luka"]
    print(f"razclenjujemo imena ...")
    razclenjena_imena = ", ".join(imena)
    print(f"narejeno!")
    return razclenjena_imena


imena = ["ajk", "andraz", "erik", "jan", "luka"]
imena_new = razcleni_imena(imena)


print(imena_new)

# print(), len(), max(), min(), ...
