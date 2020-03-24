# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def print_user(name, surname, year, city, mail, phone):
    print(f'{surname} {name}, {year} года рождения, проживает в г.{city}, его e-mail: {mail}, телефон: {phone}')


name = input('Введите имя пользователя: ')
surname = input('Введите фамилию пользователя: ')
year = input('Введите год рождения пользователя: ')
city = input('Введите город проживания пользователя: ')
mail = input('Введите e-mail пользователя: ')
phone = input('Введите номер телефона пользователя: ')

print_user(name='Иван', surname='Иванов', year='2019', city='Moscow', mail='test@test.ru', phone='+79051234567')

print_user(name=name, surname=surname, year=year, city=city, mail=mail, phone=phone)
