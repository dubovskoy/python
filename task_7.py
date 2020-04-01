# 7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки. Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с
# фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}]. Итоговый список сохранить в виде json-объекта в соответствующий файл. Пример
# json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}] Подсказка: использовать
# менеджер контекста.
import json


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f_obj:
        return f_obj.read()


def save_json(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as f_obj:
        json.dump(data, f_obj, ensure_ascii=False, indent=2)


my_dict = {}
content = read_file('text_7.txt').splitlines()
content = [el.split() for el in content]

sum_profit = 0
i = 0

for el in content:
    profit = int(el[2]) - int(el[3])
    my_dict[el[0]] = profit
    if profit >= 0:
        sum_profit += profit
        i += 1

result_list = [my_dict, {'average_profit': sum_profit / i}]
print('Итоговый список', result_list)
save_json('text_7-1.json', result_list)
