# Задание 3:
# Программа с помощью библиотеки random генерирует случайное число от 1 до 10,
# задача пользователя угадать это число за 3 попытки. В случае если пользователь
# указал больше загаданного числа, то нужно вывести "Бери меньше" и наоборот.


from random import randint

n = randint(0, 10)
i = 0
while True:
    a = int(input('Введите число:'))
    if a == n:
        print('Ты угадал!')
        break
    if a < n:
        print('Бери больше')
    else:
        print('Бери меньше')
    i += 1
    if i == 3:
        print(f'Проиграл.')
        break
