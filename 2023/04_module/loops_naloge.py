"""
1.
Napiši program, ki v neskončnost izpisuje eno in isto besedo.
"""


"""
2.
napiši program, ki samo 10x izpiše to besedo
"""


"""
3.
Napiši program, ki izpise stevila po vrsti do 20, ampak zakljuci program PRED 15.
Hint: Break
"""

# i = 0
# while i < 20:
#     i = i + 1
#     if i == 15:
#         break
#     print(f"{i}")


"""
4.
Napiši program, ki izpise stevila po vrsti do 15, ampak izpusti 4, 7, 12, 13.
Hint: Continue
"""

i = 0
while i < 15:
    i += 1
    if i in [4, 7, 12, 13]:
        continue
    print(f"{i}")

"""
5.
Napiši program, ki izpise stevila po vrsti do 30, ampak izpusti liha.
Hint: Continue
10 % 2 = 0
11 % 2 = 1
12 % 2 = 0
13 % 2 = 1
"""

"""stevec = 0
while(stevec < 10):
	print("beseda")
	stevec = stevec + 1"""

"""naredi zanko, ki se izvaja v neskončnost, in vsakič izpiše, kolikokrat se je že zgodila"""

"""stevec = 0
while(True):
	stevec = stevec +1 ---> stevec += 1
	print(stevec)"""

"""naredi program, ki uporabnika vpraša za številko in potem zanko ponovi tolikokrat , kolikor je
uporabnik vnesel. Vsakič izpiše kolikokrat je že naredil zanko"""

"""stPonovitev = input()
stPonovitev = int(stPonovitev)

stevec = 0

while(stevec < stPonovitev):
	stevec = stevec + 1
	print(stevec)"""
