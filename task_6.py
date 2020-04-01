# 6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран. Примеры строк файла: Информатика:   100(л)   50(пр)   20(
# лаб). Физика:   30(л)   —   10(лаб) Физкультура:   —   30(пр)   — Пример словаря: {“Информатика”: 170,
# “Физика”: 40, “Физкультура”: 30}


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f_obj:
        return f_obj.read()


content = read_file('text_6.txt').split()
learn = [content[i][:-1] for i in range(0, len(content), 4)]
score = [[el for el in content[i] if el.isdigit()] for i in range(0, len(content)) if i != 0 and i % 4 != 0]
score = [''.join(score[i]) for i in range(0, len(score))]

i = 0
n = 0
sum_score = 0
result = {}
for el in score:
    if i == 3:
        result[learn[n]] = sum_score
        sum_score = 0
        i = 0
        n += 1
    sum_score += int(el) if el else 0
    i += 1

print(result)
