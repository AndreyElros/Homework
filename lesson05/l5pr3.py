#Задание 3
with open('test3.txt', 'r') as my_file:
    inf = []
    a = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           a.append(i[0])
        inf.append(i[1])
print(f'Оклад меньше 20.000 у {a}, средний оклад равен {sum(map(int, inf)) / len(inf)}')