# 4)	Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, name, color, is_police):
        self._speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self._speed = 55
        print(f'{self.name} поехал')
        return self._speed

    def stop(self):
        self._speed = 0
        print(f'{self.name} стоит')

    def turn(self, direction):
        if direction == 'лево':
            print(f'{self.name} поворачивает налево')
        elif direction == 'право':
            print(f'{self.name} поворачивает направо')
        elif direction == 'прямо':
            print(f'{self.name} двигается прямо')
        elif direction == 'назад':
            print(f'{self.name} сдает назад')
        else:
            print(f'{self.name} непонятно куда едет')

    def show_speed(self):
        return self._speed


class TownCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, False)

    def show_speed(self):
        if self._speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, False)


class WorkCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, False)

    def show_speed(self):
        if self._speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, True)


town_Car = TownCar('Renault', 'Белый')
sport_Car = SportCar('Porsche', 'Красный')
work_Car = WorkCar('Ford', 'Синий')
police_Car = PoliceCar('Mercedes', 'Черно-белый')

town_Car.go()
town_Car._speed = 80
town_Car.show_speed()
town_Car.turn('лево')
town_Car.stop()

print('*'*25)

sport_Car.go()
sport_Car.turn('направо')
sport_Car.stop()

print('*'*25)

police_Car.go()
police_Car.turn('назад')
police_Car.stop()
