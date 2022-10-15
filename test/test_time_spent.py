import time
import unittest

import matplotlib.pyplot as plt

from func import calculate_date_from_file
from file_generator import FILE_DIR_ABSOLUTE_PATH, MIN_NUM, MAX_NUM


class TestTimeSpentCalcFunction(unittest.TestCase):
    """
    Проверка функций func.calculate_date_from_file
    с фиксированием времени работы теста и
    построением результирующего графика
    """

    def setUp(self):
        self.startTime = time.time()
        self.nums_count = None

    def tearDown(self):
        spent_time = time.time() - self.startTime
        spent_time = round(spent_time, 3)
        self.timer[self.nums_count] = spent_time
        print(f'{self.id}: {spent_time}')

    @classmethod
    def setUpClass(cls):
        cls.timer = {}

    @classmethod
    def tearDownClass(cls):
        lists = sorted(cls.timer.items())
        x, y = zip(*lists)
        plt.title(f'Время работы теста для чисел от {MIN_NUM} до {MAX_NUM}')
        plt.xlabel('Количество, млн. чисел')
        plt.ylabel('Время, сек')
        plt.plot(x, y)
        plt.show()

    def test_1000_nums(self):
        self.nums_count = 1000
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/{self.nums_count}.nums'
        result = calculate_date_from_file(file_path)
        self.assertIsInstance(result, tuple)

    def test_10000_nums(self):
        self.nums_count = 10000
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/{self.nums_count}.nums'
        result = calculate_date_from_file(file_path)
        self.assertIsInstance(result, tuple)

    def test_100000_nums(self):
        self.nums_count = 100000
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/{self.nums_count}.nums'
        result = calculate_date_from_file(file_path)
        self.assertIsInstance(result, tuple)

    def test_200000_nums(self):
        self.nums_count = 200000
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/{self.nums_count}.nums'
        result = calculate_date_from_file(file_path)
        self.assertIsInstance(result, tuple)

    def test_400000_nums(self):
        self.nums_count = 400000
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/{self.nums_count}.nums'
        result = calculate_date_from_file(file_path)
        self.assertIsInstance(result, tuple)

    def test_800000_nums(self):
        self.nums_count = 800000
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/{self.nums_count}.nums'
        result = calculate_date_from_file(file_path)
        self.assertIsInstance(result, tuple)

    def test_1000000_nums(self):
        self.nums_count = 1000000
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/{self.nums_count}.nums'
        result = calculate_date_from_file(file_path)
        self.assertIsInstance(result, tuple)


if __name__ == '__main__':
    unittest.main()
