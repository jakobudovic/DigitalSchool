izposojene_knjige = []  # TODO preberi iz fila

# izposojene_knjige.append("a")
# izposojene_knjige.append("b")
# izposojene_knjige.append("C")
# izposojene_knjige.remove("b")
print(f"izposojene knjige: {izposojene_knjige}")

# Branje:
# line.split(",") # ["0012", "matematika 1", "anglescina", "naravoslovje"]

user_input = input("ali zelis vrnit ali izposodit si knjigo? (i/v)")
if user_input == "i":  # izposoja
    knjiga = input("katero pa?")
    # izposojene_knjige.append(knjiga)
    with open("2023/koncni_projekti/zaloga.txt", "a") as f:
        f.write(knjiga)
        f.write("\n")

else:  # vrne
    knjiga = input("katero pa?")
    izposojene_knjige.remove(knjiga)

print(f"izposojene knjige: {izposojene_knjige}")

"""
input -> funkcija -> output
message -> fun -> seznam lihih crk
"""


def fun(message):
    seznam = []
    # TODO
    return seznam
