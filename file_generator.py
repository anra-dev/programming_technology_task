import os
import random


MIN_NUM = 1
MAX_NUM = 99
FILE_DIR = 'test_files'
TUPLE_COUNT_NUMS = (1, 10, 100, 1000, 10000, 100000, 1000000)


def generate_str_of_numbers(count_nums: int) -> str:
    """
    Генерирует строку из случайных чисел в определенном количестве.
    :param count_nums: количество чисел в строке.
    :return: срока из чисел разделенных пробелом.
    """
    list_nums = []
    while count_nums > 0:
        list_nums.append(random.randint(MIN_NUM, MAX_NUM))
        count_nums -= 1

    return ' '.join(map(str, list_nums))


def generate_file(count_nums: int):
    """
    Создает файл в который записывает строку из чисел
    :param count_nums: количество чисел
    :return: None
    """
    os.makedirs(FILE_DIR, exist_ok=True)
    file_name = f'{FILE_DIR}/{count_nums}.nums'
    with open(file_name, mode='w', encoding="utf-8") as file:
        file.write(generate_str_of_numbers(count_nums))


def generate_files_by_tuple(tuple_count_nums: tuple):
    """
    Создает файлы в которые записывает строку из чисел.
    :param tuple_count_nums: картеж с количеством чисел.
    :return: None
    """
    for count_nums in tuple_count_nums:
        generate_file(count_nums)


if __name__ == '__main__':
    generate_files_by_tuple(TUPLE_COUNT_NUMS)
