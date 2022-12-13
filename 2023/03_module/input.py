print("Kako ti je ime?")
ime = input()
print("Ime ti je", ime)

# Naredi se za priimek in visino v metrih.
print("Kako se pises?")
priimek = input()
print("Tvoj priimek je", priimek)

print("Koliko si visok v cm?")
visina_v_cm = input()
visina_v_m = int(visina_v_cm) / 100
print("ime ti je ", ime, "pises se", priimek, "Visok si", visina_v_m, "m.")

# F-string
print("Hello, %s. Your surname is %s." % (ime, priimek))
print("%s, visok si %sm" % (ime, visina_v_m))
print("{0}, visok si {2}cm oziroma {1}m.".format(ime, visina_v_m, visina_v_cm))
print(f"{ime}, visok si {visina_v_cm}cm oziroma {visina_v_m}m.")

# ime, priimek, visina_v_cm, visina_v_m
print("Ime ti je", ime, priimek)

"in pises se"


# print("ime ti je ", ime, "pises se", priimek, "Visok si", visina_v_m, "m.")


"""
Naloga
Naredi program, ki te vprasa po imenu in letu rojstva, ti pa uporabniku nato izpises, koliko je star.
"""

"Jakob, star si 19 let."
