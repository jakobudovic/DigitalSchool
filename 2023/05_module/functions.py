def my_function(name):
    print(name + " is a friend of Gent")


my_function("John")
my_function("Michael")


"""
This function says hi to a person
with the provided message
"""


def hi(name, msg):
    print("Hello", name + ", " + msg)


hi("Drin", "Morning there!")


# Calling function with argument only
hi("Gent")

# Calling function with no arguments
hi()


print("Živjo", "Filip")
print("Zivjo", "Jan")
print("Zivjo", "Tim")
print("Zivjo", "Jon")
print("Zivjo", "Jakob")


def pozdrav(name, ocena):
    print("živjo", name, ". Pisal si", ocena, ".")  # Zivjo Jakob
    print(f"Zivjo ucenec {name}. Pisal si {ocena}.")


pozdrav("Filip")
pozdrav("Jan")
pozdrav("Tim")
pozdrav("Jon")
pozdrav("Jakob")
