# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов. 23,11,55


def my_func(numb1, numb2, numb3):
    numb_list = [numb1, numb2, numb3]
    numb_list.sort()
    print(f'Сумма наибольших аргументов {numb_list[1]} и {numb_list[2]} - {sum(numb_list[1:3])}')


numbers = input('Введите 3 числа через запятую: ').split(',')
my_func(int(numbers[0]), int(numbers[1]), int(numbers[2]))
