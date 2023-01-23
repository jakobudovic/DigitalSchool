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
Hint: Continue, brez else-a
"""

# i = 0
# while i < 15:
#     i += 1
#     if i in [4, 7, 12, 13]:
#         continue
#     print(f"{i}")

"""
5.
Napiši program, ki izpise stevila po vrsti do 30, ampak izpusti liha.
Hint: Continue
10 % 2 = 0
11 % 2 = 1
12 % 2 = 0
13 % 2 = 1


17 % 5 = 2
23 % 5 = 3
103 % 5 = 3
75 % 5 = 0
if i % 5 == 0:
	print("     {i} je veckratnik!!!")
"""

# i = 0
# while i < 30:
#     i += 1
#     if i % 2 != 1:  # ce je stevilo liho
#         continue
#     print(f"{i}", end=" ")

# print(f"done")
# print(f"preostanek programa ...")


"""
Else po zakljucku loopa
"""

"""
For loop print v isto vrstico
"""
# print(f"{i}", end=" ")

"""
6.
Uporabi while loop, ki v isto vrstico izpise vse veckratnike stevila 5 do 60
"""

# i = 0
# while i < 60:
#     i += 1
#     if i % 5 == 0:
#         print(f"{i}", end=" ")


"""
7.
Izpisi vsa stevila od 1 do 60, vsak veckratnik stevila 5 izpisi s 5 zamiki v desno 
(1 zamik naj bo enako 1 presledku)
Primer:
1
2
3
4
     5
6
7
8
9
     10
...
"""


i = 0
while i < 60:
    i += 1
    if i % 5 == 0:
        # Izpis veckratnika stevila 5
        print(f"     {i}")
    else:
        # Izpis ne-veckratnika stevila 5
        print(f"{i}")


"""
8. Challenge
Create a program that sums n numbers from 1 to n and shows the result. For example: sum = 1+2+3+...+n.

Sum ... vsota
sum stevil ... vsota stevil
sum 3,5 ... 8
Za input == 5:
1 + 2 + 3 + 4 + 5 = 15

Input n

Primer programa:
Enter number: 5
The sum is: 15

Enter number: 100
The sum is: 5050

5 ... 15
10 ... 55
20 ... 210
24 ... 276
100 ... 5050
"""
