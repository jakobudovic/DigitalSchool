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


odgovor = sestej_stevilia(10, 5)
print(odgovor)


"""
A parameter is the variable listed inside the parentheses in the function definition.
An argument is a value that is sent to the function when it is called.
"""
