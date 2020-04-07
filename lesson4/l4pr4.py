#Задание 4
my_list = [3, 3, 6, 743, 743, 744, 1, 2, 1, 5]
my_new_list = [elem for elem in my_list if my_list.count(elem) < 2]
print(my_new_list)