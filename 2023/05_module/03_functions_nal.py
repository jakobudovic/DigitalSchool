"""
1. Write a function that takes in two integers and returns their sum.
"""


# def add_nums(num1, num2):
#     return num1 + num2


# rez = add_nums(3, 5)
# print(rez)

"""
2. Write a function that takes in a list of numbers and returns the average.
"""

"""
3. Write a Python function called reverse_string that takes a string as input and returns the reverse of that string. 
For example, if the input string is "hello", the function should return "olleh".
Hint: string ni nic drugega kot seznam characterjev.
"""

"""
4.
Write a Python function called is_palindrome that takes a string as input and returns True if the string is a palindrome (i.e., reads the same backward as forward), and False otherwise. 
For example, if the input string is "racecar", the function should return True.
jan != naj
jakob != bokaj
ana = ana
racecar = racecar
"""

"""
5. Write a function that takes in a string and returns a dictionary with the count of each letter in the string.
"""

# def prestej_crke(string):
#     return {}


# prestej_crke("beseda1")
# prestej_crke("beseda2")
# prestej_crke("beseda3")

"""
6. Write a function that takes in a list of integers and returns the largest and smallest numbers in the list.
def find_min_max([5, 1, 45, 12, -56, 22, 18])

Out:
print(45, -56)
"""


def find_min_max_in_list(seznam):
    # nastavi curr min in curr max na prvi element
    curr_max = seznam[0]
    curr_min = seznam[0]

    for num in seznam:  # gremo skozi vse elemente
        if num > curr_max:  # preveri, ce je stevilo vecje od nasega maksimuma
            curr_max = num
        if num < curr_min:  # preveri, ce je stevilo manjse od nasega minimuma
            curr_min = num
    return curr_min, curr_max


# min_num, max_num = find_min_max_in_list([1, 2, 3, 20, -5, 0, 23])
# print(f"rez: {min_num}, {max_num}")  # -5, 23
# min_num, max_num = find_min_max_in_list([-2, -5, -11, -56, -33, -3])
# print(f"rez: {min_num}, {max_num}")  # -56, -2
# min_num, max_num = find_min_max_in_list([2, 0, -13, 22, 1056, -34, 3])
# print(f"rez: {min_num}, {max_num}")  # -34, 1056

"""
7. Write a function that takes in two lists of integers and returns a new list with the common elements between the two lists.
Zdruzi oz. zmergaj seznama.
"""
# in:
# [5, 1, 2, 3]
# [3, 4, 5]
# out:
# [5, 1, 2, 3, 4]


def zdruzi_seznama(seznam1, seznam2):
    skupen_seznam = seznam1.copy()  # inicializiraj skupen seznam na 1. seznam

    for el in seznam2:
        if not el in skupen_seznam:  # ce elementa ni v skupnem seznamu
            # append new element to our skupen_seznam
            skupen_seznam.append(el)  # skupen_seznam = skupen_seznam + [el]
    return skupen_seznam


s1 = [5, 1, 2, 3]
s2 = [3, 4, 5]
print(f"{s1} + {s2} = {zdruzi_seznama(s1, s2)}")

s1 = [1, 2]
s2 = [3, 4, 5]
print(f"{s1} + {s2} = {zdruzi_seznama(s1, s2)}")

s1 = [1, 2, 3]
s2 = [1, 2, 3]
print(f"{s1} + {s2} = {zdruzi_seznama(s1, s2)}")

"""
8. Bonus naloga z ucenci in slovar.
"""
