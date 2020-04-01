#Задание №5
n = int(input('Введите номер: '))
my_list = [7, 5, 4, 3, 3, 2]
k = my_list.count(n)
for elem in my_list:
    if k > 0:
        i = my_list.index(n)
        my_list.insert(i + k, n)
        break
    else:
        if n > elem:
            j = my_list.index(elem)
            my_list.insert(j, n)
            break
        elif n < my_list[len(my_list) - 1]:
            my_list.append(n)
print(my_list)