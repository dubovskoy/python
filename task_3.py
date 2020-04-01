# 3)	Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#     Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f_obj:
        return f_obj.read()


content = read_file('text_3.txt').split()
average_salary = sum([float(el) for num, el in enumerate(content) if num % 2 != 0])/(len(content)/2)
top_salary = [content[num - 1] + ' ' + content[num] for num, el in enumerate(content) if num % 2 != 0 and float(el) > 20000]

print('Средний доход всех сотрудников: ', average_salary)
print('Более 20 тыс. зарабатывают: ')
[print(el) for el in sorted(top_salary)]
