# Задание №5
def my_sum():
    sum_res = 0
    n = False
    while n == False:
        number = input('Введите числа или введите Q для выхода: ').split()
        res = 0
        for elem in range(len(number)):
            if number[elem] == 'q' or number[elem] == 'Q':
                n = True
                break
            else:
                res = res + int(number[elem])
        sum_res = sum_res + res
        print(f'Текущая сумма: {sum_res}')
    print(f'Финальная сумма: {sum_res}')
my_sum()