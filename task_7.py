# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumb:
    def __init__(self, complex_numb):
        self.complex_numb = complex(complex_numb)

    def __add__(self, other):
        return self.complex_numb + other.complex_numb

    def __mul__(self, other):
        return self.complex_numb * other.complex_numb


complex1 = ComplexNumb(1 + 2j)
complex2 = ComplexNumb(3 + 4j)
print('Сложение комплексных чисел: ', complex1 + complex2)
print('Умножение комплексных чисел: ', complex1 * complex2)
