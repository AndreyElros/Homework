#Задание 2
my_list = [54, 2, 22, 22, 1, 152, 4, 10, 7, 1, 78]
my_rez_list = [elem for num, elem in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список: {my_list}')
print(f'Результат: {my_rez_list}')