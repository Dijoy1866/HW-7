# Задание 3:
# Программа с помощью библиотеки random генерирует случайное число от 1 до 10,
# задача пользователя угадать это число за 3 попытки. В случае если пользователь
# указал больше загаданного числа, то нужно вывести "Бери меньше" и наоборот.


import random

n = 0
for i in range(1, 11):

    print(f'Попытка №', n+1)
    a = int(input(':'))

    if a == i:
        print('Ты угадал!')
        break
    if a < i:
        print('Бери больше')
    else:
        print('Бери меньше')
    n += 1
    if n == 3:

        break
