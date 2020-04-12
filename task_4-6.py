# Начните работу над проектом «Склад оргтехники». Создайте класс, # описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники. Продолжить работу над первым заданием. Разработать методы,
# отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о
# наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем
# данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


class Storage:
    def __init__(self):
        self.dic = {}

    def add(self, Equip, amount, division):
        if type(amount) == int:
            if not self.dic.get(division):
                self.dic = {division: {Equip.type_equip: {Equip.name: amount}}}
            elif not self.dic[division].get(Equip.type_equip):
                self.dic[division].update({Equip.type_equip: {Equip.name: amount}})
            elif not self.dic[division][Equip.type_equip].get(Equip.name):
                self.dic[division][Equip.type_equip].update({Equip.name: amount})
            else:
                self.dic[division][Equip.type_equip][Equip.name] += amount
        else:
            print('Неверно указано количество')

    def show(self):
        print('Оборудование на складах: ', self.dic)

    def transfer(self, Equip, amount, division_out, division_in):
        if self.dic[division_out][Equip.type_equip][Equip.name] >= amount:
            self.dic[division_out][Equip.type_equip][Equip.name] -= amount
            if not self.dic.get(division_in):
                self.dic.update({division_in: {Equip.type_equip: {Equip.name: 0}}})
            elif not self.dic[division_in].get(Equip.type_equip):
                self.dic[division_in].update({Equip.type_equip: {Equip.name: 0}})
            elif not self.dic[division_in][Equip.type_equip].get(Equip.name):
                self.dic[division_in][Equip.type_equip].update({Equip.name: 0})
            self.dic[division_in][Equip.type_equip][Equip.name] += amount
        else:
            print('Ошибка перемещения')


class Equipment:
    def __init__(self, type_equip, name):
        self.type_equip = type_equip
        self.name = name


class Printer(Equipment):
    def __init__(self, type_equip, name, print_speed):
        super().__init__(type_equip, name)
        self.print_speed = print_speed


class Scanner(Equipment):
    def __init__(self, type_equip, name, scan_speed):
        super().__init__(type_equip, name)
        self.scan_speed = scan_speed


class Xerox(Equipment):
    def __init__(self, type_equip, name, copy_speed):
        super().__init__(type_equip, name)
        self.copy_speed = copy_speed


if __name__ == '__main__':
    printer = Printer('HP', 'LaserJet', 35)
    scan = Scanner('HP', 'scanner', 10)
    xerox = Xerox('HP', 'copier', 20)
    mfu = Xerox('Samsung', 'MFU', 120)
    m = Storage()
    print('Добавляем оборудование на склад: ')
    m.add(printer, 19, 'Склад')
    m.add(scan, 43, 'Склад')
    m.add(scan, 13, 'Склад')
    m.add(xerox, 22, 'Склад')
    m.add(xerox, 111, 'Склад')
    m.add(mfu, 36, 'Склад')
    m.show()
    print('Перемещаем оборудование в подразделение:')
    m.transfer(xerox, 53, 'Склад', 'Ц.офис')
    m.transfer(mfu, 15, 'Склад', 'Ц.офис')
    m.show()
