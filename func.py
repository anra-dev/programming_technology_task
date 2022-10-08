def get_data_from_file(file_path: str) -> str:
    """
    Возвращаем данные из файла.
    :param file_path: путь к файлу.
    :return: данные в текстовом формате.
    """
    with open(file_path) as file:
        data = file.readline().strip()
    return data


def get_tuple_of_numbers(data: str) -> tuple[int]:
    """
    Преобразует строку, разделенную пробелами, в список чисел.
    :param data: строка в формате "3 89 56 7".
    :return: список чисел или None если преобразование не удалось.
    """
    tuple_of_numbers = None
    try:
        tuple_of_numbers = tuple(int(i) for i in data.split())
    except ValueError as e:
        print("File data is not correct")
    return tuple_of_numbers


def _min(data: tuple[int]) -> int:
    """
    Возвращает минимальное число из кортежа чисел.
    :param data: кортеж, где все элементы числа.
    :return: минимальное число.
    """
    result = data[0]
    for i in range(1, len(data)):
        if data[i] < result:
            result = data[i]
    return result


def _max(data: tuple[int]) -> int:
    """
    Возвращает максимальное число из кортежа чисел.
    :param data: кортеж, где все элементы числа.
    :return: максимальное число.
    """
    result = data[0]
    for i in range(1, len(data)):
        if data[i] > result:
            result = data[i]
    return result


def _sum(data: tuple[int]) -> int:
    """
    Суммирует элементы кортежа.
    :param data: кортеж, где все элементы числа.
    :return: число - сумму всех элементов.
    """
    result = 0
    for item in data:
        result += item
    return result


def _mult(data: tuple[int]) -> int:
    """
    Перемножает элементы кортежа.
    :param data: кортеж, где все элементы числа.
    :return: число - произведение всех элементов.
    """
    result = None
    for item in data:
        if result is None:
            result = item
        else:
            result *= item
    return result


def main():
    """
    Считывает из файла числа, а далее ищет среди этих чисел
    минимальное число, максимальное число, считать их
    общую сумму и произведение.
    :return:
    """
    file_path = "numbers.txt"
    data_from_file = get_data_from_file(file_path)
    nums = get_tuple_of_numbers(data_from_file)
    if nums is not None:
        print(_min(nums))
        print(_max(nums))
        print(_sum(nums))
        print(_mult(nums))


if __name__ == '__main__':
    main()
