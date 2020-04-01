# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
text = 1
result = ''


def save_file(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as f_obj:
        f_obj.write(data)


while text:
    text = input('Введите данные для записи в файл (окончание ввода - пустая строка): ')
    result += text + '\n'

print('Данные записанные в файл:\n', result)
save_file(result, 'text_1.txt.')
