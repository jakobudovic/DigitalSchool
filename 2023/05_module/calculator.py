"""
Naredi program, ki sprejme dve stevili in operator, 
ter vrne rezultat racuna teh dveh stevil z operatorjem.
Program mora podpirati vsaj +, -, * in /
Bonus funkcionalnosti: %, //, **
"""

# izracunaj(3, 6, "*")  # 18
# izracunaj(18, 6, "-")  # 12


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
        print(f"Operacija {operator} ni podprta.")


print(izracunaj(5, 2, "+"))
print(izracunaj(5, 2, "**"))
print(izracunaj(9, 2, "koren"))
print(izracunaj(9, 2, "&"))

# ime = "Jakob"
# age = 23
# naj_igrice = ["gtaV", "amogus", "ovecooked"]
# print("Zivjo ime mi je " + ime + " In star si" + str(age) + ".")
# print("Zivjo ime mi je", ime, "In star si", age, ".")
# print(f"Zivjo ime mi je {ime} in star si {age}. Cez 5 let bos star {age + 5}")
# print(f"Najljubsa igrica je {naj_igrice[0]}")

# print(f"{age}")
