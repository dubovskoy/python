# 5)	Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
#     Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as f_obj:
        [f_obj.write(str(el) + ' ') for el in range(1, 100, 8)]


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f_obj:
        return f_obj.read()


file = 'text_5.txt'
create_file(file)
content = [int(el) for el in read_file(file).split()]
print(f'Числа в файле: {content}')
print(f'Сумма чисел в файле {sum(content)}')
