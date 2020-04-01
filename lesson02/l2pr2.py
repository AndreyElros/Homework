#Задание №2
a = [int(s) for s in input('Введите элементы списка через пробел: ').split()]
for s in range(1, len(a), 2):
    a[s - 1], a[s] = a[s], a[s - 1]
print(' '.join([str(s) for s in a]))