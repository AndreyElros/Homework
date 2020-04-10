#Задание 4
ru = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('test4.txt', 'r') as file_one:
    for i in file_one:
        i = i.split(' ', 1)
        new_file.append(ru[i[0]] + '  ' + i[1])
    print(new_file)

with open('test4_new.txt', 'w') as file_two:
    file_two.writelines(new_file)