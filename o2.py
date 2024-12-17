import math

antall_elever = int(input('Hvor mange elever er det i klassen? '))
pizzaer = math.ceil(antall_elever / 4)
print(f'Det trengs {pizzaer} pizzaer til klassen.')