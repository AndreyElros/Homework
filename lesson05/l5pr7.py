#Задание 7
import json
vigod = {}
a = {}
rez = 0
rez_mid = 0
i = 0
with open('test7.txt', 'r') as file:
    for line in file:
        firm, simb, viruch, less = line.split()
        vigod[firm] = int(viruch) - int(less)
        if vigod.setdefault(firm) >= 0:
            rez = rez + vigod.setdefault(firm)
            i += 1
    if i != 0:
        rez_mid = rez / i
        print(f'Средняя прибыль: {rez_mid:.2f}')
    else:
        print(f'Средняя прибыль отсутсвует. Работа в убыток!')
    a = {'Средняя прибыль': round(rez_mid)}
    vigod.update(a)
    print(f'Прибыль каждой компании - {vigod}')

with open('test7.json', 'w') as write_js:
    json.dump(vigod, write_js)

    js_str = json.dumps(vigod)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')