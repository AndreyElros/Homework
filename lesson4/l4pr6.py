#Задание 6
# a)
from itertools import count

for elem in count(int(input('Введите первое число: '))):
    if elem > 123:
        break
    else:
        print(elem)

# b)
from itertools import cycle

count = 0
my_list = [None, False, 'String', 123]
for elem in cycle(my_list):
    if count > 10:
        break
    print(elem)
    count += 1