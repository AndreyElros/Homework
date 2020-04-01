#Задание №4
my_s = input('Введите строку: ')
a = my_s.split(' ')
for i, elem in enumerate(a, 1):
    if len(elem) > 10:
        elem = elem[0:10]
    print(i, elem)