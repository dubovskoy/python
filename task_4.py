# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите число: '))
max_number = 0

print(f'Наибольшая цифра в числе {number}: ')

while number > 0:
    n = number % 10
    number = number // 10
    if n > max_number:
        max_number = n

print('****', max_number, '****')
