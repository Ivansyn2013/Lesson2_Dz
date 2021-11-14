# третье задание второго урока

base_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']

names_list_temp = []
names = []
i = 0

for el in base_list:
    el = str(el)
    names_list_temp.append(el.split(' '))
    names.append(names_list_temp[i].pop())
    names[i] = names[i].capitalize()
    print('Привет, ', names[i], '!', sep='')

    i += 1
