
# Вопрос №2:
# Задание:
#
# Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по
# радиусу и треугольника по трем сторонам. Дополнительно к работоспособности оценим:
#
# Юнит-тесты
# Легкость добавления других фигур
# Вычисление площади фигуры без знания типа фигуры в compile-time
# Проверку на то, является ли треугольник прямоугольным

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """ Абстрактный класс для определения всех фигур """
    @abstractmethod
    def area(self):
        print('Метод надо переопределить')
        raise NotImplementedError('Метод area() надо переопределить')


class Circle(Shape):
    """ Класс круга """
    def __init__(self, data_1):
        self.data_1 = data_1

    def area(self):
        result = math.pi * (self.data_1 ** 2)
        return f"Площадь круга: {result}"


class Triangle(Shape):
    """ Класс треугольника """
    def __init__(self, data_1, data_2, data_3):
        self.data_1 = data_1
        self.data_2 = data_2
        self.data_3 = data_3

        if not (data_1 + data_2 > data_3 and data_1 + data_3 > data_2 and data_2 + data_3 > data_1):
            raise ValueError("Стороны треугольника указаны неверно")

    def area(self):
        p = (self.data_1 + self.data_2 + self.data_3) / 2
        result = math.sqrt(p * (p - self.data_1) * (p - self.data_2) * (p - self.data_3))
        return f"Площадь треугольника: {result}"

    def check_triangle(self):
        s = sorted([self.data_1, self.data_2, self.data_3])
        return 'Прямоугольный' if s[0] * s[0] + s[1] * s[1] == s[2] * s[2] else 'Не прямоугольный'


class Rectangle(Shape):
    """ Класс прямоугольника как доп фигура"""
    def __init__(self, data_1, data_2):
        self.data_1 = data_1
        self.data_2 = data_2

    def area(self):
        result = self.data_1 * self.data_2
        return f"Площадь прямоугольника: {result}"


def area_calculation(*args):
    """ Функция вычисления площади фигуры без знания типа фигуры в compile-time """
    if len(args) == 1:
        return Circle(*args).area()
    if len(args) == 2:
        return Rectangle(*args).area()
    if len(args) == 3:
        result = Triangle(*args).area()
        result_check = Triangle(*args).check_triangle()
        return f"{result}, {result_check}"
    if len(args) > 3:
        raise NotImplementedError(
            "Метод фигуры не реализован!"
        )


if __name__ == '__main__':
    test = area_calculation(10, 15, 20)
    print(test)
