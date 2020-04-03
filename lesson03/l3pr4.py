# Задание №4
def my_func(a, b):
    n = 1
    for i in range(abs(b)):
        n *= a
    if b >= 0:
        return n
    else:
        return 1 / n
print(my_func(float(input('Введите положительное число: ')), int(input('Введите отрицательное число: '))))