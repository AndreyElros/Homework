#Задание №6
goods = []
features = {'название': '', 'цена': '', 'количество': '', 'ед': ''}
analytic = {'название': [], 'цена': [], 'количество': [], 'ед': []}
n = 0
my_feature = None
control = None
my_list = []
while True:
    control = input("Для выхода введите 'Q', для ввода информации введите 'C', для вывода аналитики введите 'A': ").upper()
    if control == 'Q':
        break
    n += 1
    if control == 'C':
        for f in features.keys():
            feature_ = input(f'Введите параметр "{f}": ')
            features[f] = int(my_feature) if (f == 'цена' or f == 'количество') else my_feature
            analytic[f].append(features[f])
            my_list = dict(features)
        goods.append(my_list)
    if control == 'A':
        print('Акутальная аналитика: ')
        for i, elem in enumerate(goods, start=1):
            print(f'({i}, {elem})')
        for key, value in analytic.items():
            print(f'{key}: {value}')