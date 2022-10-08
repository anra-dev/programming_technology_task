import unittest
from func import _min, _max, _sum, _mult, get_tuple_of_numbers


TEST_DATA_LIST = [
    {
        'data_str': '1 2 3 4 5',
        'data': (1, 2, 3, 4, 5),
        'min': 1,
        'max': 5,
        'sum': 15,
        'mult': 120,
    },
    {
        'data_str': '0 2 23 4 5',
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
        for test_data in TEST_DATA_LIST:
            self.assertEqual(_min(test_data['data']), test_data['min'])

    def test_max(self):
        """
        Тестирование функции func._max
        """
        for test_data in TEST_DATA_LIST:
            self.assertEqual(_max(test_data['data']), test_data['max'])

    def test_sum(self):
        """
        Тестирование функции func._sum
        """
        for test_data in TEST_DATA_LIST:
            self.assertEqual(_sum(test_data['data']), test_data['sum'])

    def test_mult(self):
        """
        Тестирование функции func._mult
        """
        for test_data in TEST_DATA_LIST:
            self.assertEqual(_mult(test_data['data']), test_data['mult'])

    def test_tuple_of_numbers(self):
        """
        Тестирование функции func.get_tuple_of_numbers

        дополнительный тест
        """
        for test_data in TEST_DATA_LIST:
            tuple_of_numbers = get_tuple_of_numbers(test_data['data_str'])
            self.assertIsInstance(tuple_of_numbers, tuple)
            self.assertTupleEqual(tuple_of_numbers, test_data['data'])


if __name__ == '__main__':
    unittest.main()
