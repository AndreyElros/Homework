#Задание 6
subj = {}
import re
with open('test6.txt', 'r') as init_f:
        for line in init_f:
            subject, lecture, practice, lab = line.split()
            l = sum(map(int, re.findall(r"\d+", lecture)))
            p = sum(map(int, re.findall(r"\d+", practice)))
            n_l = sum(map(int, re.findall(r"\d+", lab)))
            subj[subject] = l + p + n_l
print(f'Общее количество часов по предмету: \n {subj}')