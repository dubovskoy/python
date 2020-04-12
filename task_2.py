# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class MyZeroDivisionError(Exception):
    def __init__(self, message):
        self.message = message


try:
    a, b = map(int, input('Введите делимое(a) и делитель(b): ').split())
    if b == 0:
        raise MyZeroDivisionError('Запрещено делить на ноль!')
    print(f'Result: {a / b:.2f}')
except MyZeroDivisionError as e:
    print(e)
except ValueError as e:
    print('Ошибка значения!')
