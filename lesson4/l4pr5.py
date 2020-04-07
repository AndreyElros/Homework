#Задание 5
from functools import reduce
def my_func(elem_p, elem):
    return elem_p * elem
print(f'Список четных значений: {[elem for elem in range(99, 1001) if elem % 2 == 0]}')
print(f'Результат перемножения всех элементов списка: {reduce(my_func, [elem for elem in range(99, 1001) if elem % 2 == 0])}')