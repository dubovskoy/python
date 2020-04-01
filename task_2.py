# 2)	Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f_obj:
        return f_obj.read()


content = read_file('text_2.txt')

print(f'Строк в файле: {len(content.splitlines())}')
[print(f'Строка {num} слов: {len(el.split())}') for num, el in enumerate(content.splitlines(), 1)]
