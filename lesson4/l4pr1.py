#Задание 1
def rez():
    try:
        vir = float(input('Выработка в часах: '))
        stavka = int(input('Ставка в час: '))
        prem = int(input('Премия: '))
        res = vir * stavka + prem
        print(f'Заработная плата сотрудника:  {res}')
    except ValueError:
        return print('Not a number')
rez()