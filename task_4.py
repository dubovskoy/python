# 4)	Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4 Необходимо
# написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


def format_file(file_name, file_new):
    result = ''
    num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять', 'Six': 'Шесть',
                'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять'}
    with open(file_name, 'r', encoding='utf-8') as f_obj:
        for el in f_obj:
            el = el.split()
            result += num_dict[el[0]] + ' ' + el[1] + ' ' + el[2] + '\n'

    with open(file_new, 'w', encoding='utf-8') as f_new:
        f_new.write(result)
    print(f'В файл {file_new} записана информация: \n {result}')


format_file('text_4.txt', 'text_4-1.txt')
