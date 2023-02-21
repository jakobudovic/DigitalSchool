"""
Naredi 4 funkcije, ki sprejmejo 2 stevili in vrnejo njuno 
- vsoto
- razliko
- zmnozek 
- kolicnik

potenca a^b; npr. a^5 = a * a * a * a * a
koren b - stopnja korena, a - tisto kar se koreni.
celostevilsko deljenje (//)
ostanek pri deljenju (%)
"""


def vsota(a, b):
    return a + b


def razlika(a, b):
    return a - b


"""
Naredi funkcijo, ki sprejme dve stevili in operator, 
ter vrne rezultat racuna teh dveh stevil z operatorjem.
Program mora podpirati vsaj +, -, * in /
Bonus funkcionalnosti: %, //, **, koren
"""

# izracunaj(-2, 7, "+")  # 5
# izracunaj(18, 6, "-")  # 12
# izracunaj(3, -6, "*")  # -18
# izracunaj(45, 3, "/")  # 15
# izracunaj(3, 12, "*")  # 35


def vsota(a, b):
    return a + b


def potenca(a, b):
    return a**b


def koren(a, b):
    return a ** (1 / b)


# def odstej
# ...


def izracunaj(a, b, operator):
    if operator == "+":
        return vsota(a, b)
    elif operator == "**":
        return potenca(a, b)
    elif operator == "koren":
        return koren(a, b)
    else:
        print(f"Operacija '{operator}' ni podprta.")


print(izracunaj(5, 2, "+"))
print(izracunaj(5, 2, "**"))
print(izracunaj(9, 2, "koren"))
print(izracunaj(9, 2, "&"))
