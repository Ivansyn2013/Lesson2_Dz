# первое задание второго урока.
# задание
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

# второе задание второго урока

data_input = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_data = []

# перебераем элементы, выделяем цыфры, добавляем ковычки
for el in data_input:
    i = 0
    if el.isdigit() == True:
        new_data.append('"')
        new_data.append(int(el))
        new_data.append('"')
    else:
        if len(el) != 1:
            el_ex = list(el)
            for el_in in el_ex:
                i += 1

                if el_in.isdigit() == True or el_in == '+' or el_in == '-':
                    new_data.append('"')
                    # ищем дополнительные знаки, отдельно сохраняем температуру
                    if el_in == '+':
                        new_data.append('+')
                    elif el_in == '-':
                        new_data.append('-')

                    new_data.append(int(el))
                    new_data.append('"')
                    break
                elif el_in.isdigit() != True and i < len(el_ex):
                    continue
                elif i == len(el_ex):
                    new_data.append(el)
                    break
        else:
            new_data.append(el)
i = 1
for el_print in new_data:

    if type(el_print) == int:
        print(f'{(el_print):02d}', end='', sep='')
    else:
        if el_print == '"':
            i += 1
            if el_print == '"' and i % 2 == 0:
                print(el_print, end='')
            elif el_print == '"' and i % 2 != 0:
                print(el_print, end=' ')
        else:
            print(el_print, end=' ')
