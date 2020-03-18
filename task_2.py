# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input('Введите время в секундах: '))

hours = seconds // 3600
minutes = (seconds - (hours * 3600)) // 60
sec = seconds - (hours * 3600) - (minutes * 60)

print(seconds, 'секунд это', f'{hours:02}:{minutes:02}:{sec:02}')
# print(seconds, 'секунд это', '{:02}:{:02}:{:02}'.format(hours, minutes, sec))
# print(seconds, 'секунд это', '%02d:%02d:%02d' % (hours, minutes, sec))
