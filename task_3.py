# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

season_list = ['', 'Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
season_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень',
               10: 'Осень', 11: 'Осень', 12: 'Зима'}

month_number = int(input('Введите номер месяца: '))
if 1 <= month_number <= 12:
    print(f'Список. Месяц -={month_number}=- относится к времени года: {season_dict[month_number]}')
    print(f'Словарь. Месяц -={month_number}=- относится к времени года: {season_list[month_number]}')
else:
    print(f'Месяца с номером -={month_number}=- не существует.')
