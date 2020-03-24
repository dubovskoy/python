# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(numb_1, numb_2):
    result = 0
    try:
        result = numb_1 / numb_2
    except ZeroDivisionError:
        print('Делить на 0 нельзя')
    return result


user_numb_1 = int(input('Введите делимое: '))
user_numb_2 = int(input('Введите делитель: '))

print(f'{user_numb_1}/{user_numb_2} = {division(user_numb_1, user_numb_2):.2f}')
