#Задание №2
def my_func (name, surname, year, town, email, telephone):
     return ' '.join([name, surname, year, town, email, telephone])
print(my_func(surname = 'Ivanov', telephone = '+7-905-814-22-22', year = '1993', town = 'Vladimir', name = 'Ivan', email = 'example@gmail.ru'))
