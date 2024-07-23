import unittest
from Z_Mindbox_test.task_1.task import area_calculation


class TestShape(unittest.TestCase):
    """ Тестируем вычисления площади"""
    def test_area_calculation(self):
        test_data = {(4, ): 'Площадь круга: 50.26548245743669',
                     (4, 2): 'Площадь прямоугольника: 8',
                     (4, 5, 6): 'Площадь треугольника: 9.921567416492215, Не прямоугольный'}
        for numbers, result in test_data.items():
            self.assertEqual(area_calculation(*numbers), result)

    def test_not_implemented(self):
        """ Тестируем неверные данные фигуры"""
        with self.assertRaises(NotImplementedError):
            area_calculation(1, 2, 3, 4)

    def test_triangle(self):
        """ Тестируем на треугольник """
        with self.assertRaises(ValueError):
            area_calculation(1, 2, 3)

    def test_check_triangle(self):
        """ Тестируем является ли треугольник прямоугольным. """
        test_data = {
            (3, 4, 5): 'Площадь треугольника: 6.0, Прямоугольный',
            (5, 4, 2): 'Площадь треугольника: 3.799671038392666, Не прямоугольный',
            (10, 15, 20): 'Площадь треугольника: 72.61843774138907, Не прямоугольный',
        }
        for numbers, result in test_data.items():
            self.assertEqual(area_calculation(*numbers), result)


if __name__ == '__main__':
    unittest.main()
