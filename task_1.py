# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у
# пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

Hello = 'Hello'
var23 = 23

print('Hello 23')
print(Hello, var23)
print(Hello + ' ' + str(var23))

name = input('Введите свое имя: ')
age = int(input('Введите ваш возраст: '))
year = 2020 - age
print(f'Здравствуйте {name}, вы родились в {year}г.')

password = '123456'
password_or = input('Введите пароль: ')
if password == password_or:
    print('Пароль введен верно')
    int1 = int(input('Введите число (1): '))
    int2 = int(input('Введите число (2): '))
    print('Сумма введенных чисел: ', int1 + int2)
else:
    print('Неверный пароль')
