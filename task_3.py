# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input('Введите число: ')

numberX = int(number)
numberXX = int(number + number)
numberXXX = int(number + number + number)

number_sum = numberX + numberXX + numberXXX

print(f'Сумма чисел ({numberX} + {numberXX} + {numberXXX}) =', number_sum)
