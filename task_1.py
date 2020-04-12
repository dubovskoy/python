# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.


class Date:

    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def ext_date(cls, param):
        day, month, year = map(int, param.split('-'))
        return day, month, year

    @staticmethod
    def valid_date(str_date):
        list_date = Date.ext_date(str_date)
        return True if 0 < list_date[0] <= 31 and 0 < list_date[1] <= 12 and 1900 < list_date[2] <= 2020 else False

    def valid_date_norm(self):
        print('Корректная дата') if Date.valid_date(self.str_date) else print('Некорректная дата')


if __name__ == '__main__':
    my_date = Date('28-12-2019')
    print('Извлекаем дату: ')
    print(my_date.ext_date(my_date.str_date))
    print('Проверяем дату: ')
    my_date.valid_date_norm()
