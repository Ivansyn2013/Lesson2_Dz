# четвертое задание второго урока
import random

i = 0
price = []

print('Список цен:')
while i < 20:
    # случайный список цен
    price.append(random.uniform(10, 100))
    print(f' {price[i] // 1:.0f} руб. {int(price[i] % 1 * 100):02d} коп.', end=',')

    i += 1
print('\nПо возрастанию')
price.sort()
for i in price:
    print(f' {i // 1:.0f} руб. {int(i % 1 * 100):02d} коп.', end=',')
# новый список
copy_price = price.copy()
# по убыванию
copy_price.reverse()

print('\nПо убыванию')
for i in copy_price:
    print(f' {i // 1:.0f} руб. {int(i % 1 * 100):02d} коп.', end=',')

print('\n5 самых дорогих')
flag = 0
for i in copy_price:
    print(f' {i // 1:.0f} руб. {int(i % 1 * 100):02d} коп.', end=',')
    flag += 1
    if flag == 5:
        break
# для проверки

print(f'\n\n\n контрольные значения\n {price}', end=',')
