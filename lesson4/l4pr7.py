#Задание 7
from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)

n = 0
for el in fact():
    if n < 4:
        print(el)
        n += 1
    else:
        break