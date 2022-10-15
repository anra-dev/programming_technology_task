import time
import unittest

from func import calculate_date_from_file
from file_generator import FILE_DIR_ABSOLUTE_PATH


class TestTimeSpentCalcFunction(unittest.TestCase):
    """
    Проверка функций func.calculate_date_from_file
    с фиксированием времени работы теста
    """
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        spent_time = time.time() - self.startTime
        print(f'{self.id}: {spent_time:.3f}')

    def test_1000_nums(self):
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/1000.nums'
        result = calculate_date_from_file(file_path)
        self.assertIsInstance(result, tuple)

    def test_10000_nums(self):
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/10000.nums'
        result = calculate_date_from_file(file_path)
        self.assertIsInstance(result, tuple)

    def test_100000_nums(self):
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/100000.nums'
        result = calculate_date_from_file(file_path)
        self.assertIsInstance(result, tuple)

    def test_200000_nums(self):
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/200000.nums'
        result = calculate_date_from_file(file_path)
        self.assertIsInstance(result, tuple)

    def test_400000_nums(self):
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/400000.nums'
        result = calculate_date_from_file(file_path)
        self.assertIsInstance(result, tuple)

    def test_800000_nums(self):
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/800000.nums'
        result = calculate_date_from_file(file_path)
        self.assertIsInstance(result, tuple)

    def test_1000000_nums(self):
        file_path = f'{FILE_DIR_ABSOLUTE_PATH}/1000000.nums'
        result = calculate_date_from_file(file_path)
        self.assertIsInstance(result, tuple)


if __name__ == '__main__':
    unittest.main()
