import unittest
from func import _min, _max, _sum, _mult


test_data_list = [
    {
        'data': (1, 2, 3, 4, 5),
        'min': 1,
        'max': 5,
        'sum': 15,
        'mult': 120,
    },
    {
        'data': (0, 2, 23, 4, 5),
        'min': 0,
        'max': 23,
        'sum': 34,
        'mult': 0,
    },
]


class MyTestCase(unittest.TestCase):
    """
    Проверка вспомогательных функций модуля func
    """
    def test_min(self):
        """
        Тестирование функции func._min
        """
        for test_data in test_data_list:
            self.assertEqual(_min(test_data['data']), test_data['min'])

    def test_max(self):
        """
        Тестирование функции func._max
        """
        for test_data in test_data_list:
            self.assertEqual(_max(test_data['data']), test_data['max'])

    def test_sum(self):
        """
        Тестирование функции func._sum
        """
        for test_data in test_data_list:
            self.assertEqual(_sum(test_data['data']), test_data['sum'])

    def test_mult(self):
        """
        Тестирование функции func._mult
        """
        for test_data in test_data_list:
            self.assertEqual(_mult(test_data['data']), test_data['mult'])


if __name__ == '__main__':
    unittest.main()
