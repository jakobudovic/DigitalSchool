"""nariši kvadrat iz zvezdic ki je tako velik kolikor reče uporabnik"""

"""velikost = int(input())
for i in range(velikost):
	zvezda = ""
	for j in range(velikost): # --> ta cela zanka je isto kot zvezda = "* " * velikost
		zvezda += "* "
	print(zvezda)"""


"""nariši kvadat, ki je za to isto velikost zamaknjen v sredo konzole
   * * *
   * * *
   * * *"""
"""print("-----------")
velikost = int(input())
for i in range(velikost):
	print((" "*velikost) + ("* " * velikost))"""

"""Napiši program, ki nariše poljuben lik; --> program uprasa uporabnika
in uproabnik vsene stevilko lika, potem vnese velikost --> pri vsakemu 
liku na dnu izpišete še površino
Uporabnik lahko izbira med
1. Kvadrat
2. Pravokotnik
3. Pravokotni trikotnik
*
**
***
4. Navaden trikotnik  (primer visina = 4)
   * i = 0 ---> 1
  *** i = 1 ---> 3
 ***** i = 2 ---> 5
******* i = 3 ---> 7
5. obrnjen navaden trikotnik (primer visina = 3)
***** i = 0 --- > 5 --->  2*(3 - (0+1)) +1 == 5
 *** i = 1 ---- > 3 --->  2*(velikost - (i+1)) + 1
  * i = 2 ----- > 1 --->  2*(velikost - (i+1)) + 1
6. božična smrekica	(primer visina = 3)
   *
  ***
   *
  ***
 *****
   *
  ***
 *****
*******

7. Davidova zvezda (primer visina = 2)

    *
   ***
*********  visina 2 ---> 9 zvezdic
 *******
*********
   ***
    *

       * visina = 3
      ***
     *****
***************  visina 3 ---> 15 zvezdic
 *************
  ***********
 *************
***************
     *****
      ***
       *
    """

#print("-----------")

print("Kateri lik naj izrišem?")
print("1. Kvadrat")
print("2. Pravokotnik")
print("3. Pravokotni trikotnik")
print("4. Navaden trikotnik, enakostranični")
print("5. Navaden trikotnik, enakostranični, obrnjen na glavo")
print("6. Božična smrekca")
print("7. Davidova zvezda")

lik = int(input("Vnesi lik: "))

if(lik == 1): #kvadrat
   velikost = int(input("Velikost: "))
   for i in range(velikost):
      print("* " * velikost)
   print("Povrsina: " + str(velikost*velikost))


elif(lik == 2): #pravokotnik
   visina = int(input("Višina: "))
   sirina = int(input("Širina: "))
   
   for i in range(visina):
      print(sirina * "* ")

   print("Povrsina: " + str(visina*sirina))

elif(lik == 3): #pravokoten trikotnik
   velikost = int(input("Velikost: "))

   povrsina = 0
   for i in range(velikost): # velikost = 3 ---> 0, 1, 2  , i = 0, i = 1, i = 2
      print((i+1) * "* ")
      povrsina += i+1

   print("Povrsina: " + str(povrsina))

elif(lik == 4): #enakostranicen trikotnik
   velikost = int(input("Velikost: "))

   povrsina = 0
   for i in range(velikost):
      print((velikost-i -1)* " " +  (1+ 2*i)*"*")
      povrsina += (1+ 2*i)

   print("Povrsina: " + str(povrsina))
   print()

   for i in range(velikost):
      print((velikost-i -1)* " " +  (i+1)*"* ")

elif(lik == 5): #enakostraničen narobe obrnjen
   velikost = int(input("Velikost: "))

   povrsina = 0
   for i in range(velikost): #(velikost, -1, -1) ---> 1+ 2*1
      print(i*" " + (2*(velikost - (i+1)) +1) * "*")
      povrsina += (2*(velikost - (i+1)) +1)

   print("Povrsina :" + str(povrsina))

   print()

   for i in range(velikost):
      print(i*" " + (velikost - i) * "* ")


elif(lik == 6): #Božična smrekca
   velikost = int(input("Velikost: "))

   povrsina = 0
   for i in range(velikost):
      visinaSmrekce = i + 2

      for j in range(visinaSmrekce):
         print((velikost - i - 1) * " " + (visinaSmrekce - j -1) * " " + (1+ 2*j) * "*")
         povrsina += (1+ 2*j)


   print("Povrsina :" + str(povrsina))
   print()

   for i in range(velikost):
      visinaSmrekce = i + 2

      for j in range(visinaSmrekce):
         print((velikost - i - 1) * " " +(visinaSmrekce-j -1)* " " +  (j+1)*"* ")


elif(lik == 7): #Davidova zvezda
   velikost = int(input("Velikost: "))

   povrsina = 0
   #Risanje zgornjega dela
   for i in range(velikost):
      print((1 + 2*(velikost-1)) * " " + (velikost-i -1)* " " +  (1+ 2*i) * "*")
      povrsina += (1+ 2*i)

   #Risanje srednjega dela
   #dolzina prve vrstice  ---> 3x dolžina spodnje vrstice trikotnika ---> (1 + 2*(velikost-1))*3 - i * 2
   for i in range(velikost):
      print(" " * i + ((1 + 2*(velikost-1))*3 - i * 2) * "*")
      povrsina += ((1 + 2*(velikost-1))*3 - i * 2)

   for i in range(velikost -1):
      razlika = ((velikost -1) - i)-1
      print(" " * razlika + ((1 + 2*(velikost-1))*3 - razlika * 2) * "*")
      povrsina += ((1 + 2*(velikost-1))*3 - razlika * 2)

   #Risanje spodnjega dela
   for i in range(velikost):
      print((1 + 2*(velikost-1)) * " " + i*" " + (2*(velikost - (i+1)) +1) * "*")
      povrsina += (2*(velikost - (i+1)) +1)

   print("Povrsina :" + str(povrsina))
   print()


   #Risanje zgornjega dela
   for i in range(velikost):
      print((1 + 2*(velikost-1)) * " " + (velikost-i -1)* " " +  (i+1)*"* ")

   #Risanje srednjega dela
   #dolzina prve vrstice  ---> 3x dolžina spodnje vrstice trikotnika ---> (1 + 2*(velikost-1))*3 - i * 2
   for i in range(velikost):
      print(" " * i + ((3*(velikost)-i)-1) * "* ")

   for i in range(velikost -1):
      razlika = ((velikost -1) - i)-1
      print(" " * razlika + (3*(velikost)-razlika - 1) * "* ")

   #Risanje spodnjega dela
   for i in range(velikost):
      print((1 + 2*(velikost-1)) * " " + i*" " + (velikost - i) * "* ")


elif(lik > 7):
   print("Niste vnesli veljavnega lika >:(")