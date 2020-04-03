#Задание №1
def my_f(*args):
    try:
        n1 = int(input('Введите делимое: '))
        n2 = int(input('Введите делитель: '))
        a = n1 / n2
    except ValueError:
        return 'Ошибка значения'
    except ZeroDivisionError:
        return 'Неверный делитель!!! На 0 делить нельзя!'
    return a
print(f'Результат:  {my_f()}')
