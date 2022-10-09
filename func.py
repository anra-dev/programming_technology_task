def get_data_from_file(file_path: str) -> str:
    """
    Возвращаем данные из файла.
    :param file_path: путь к файлу.
    :return: данные в текстовом формате.
    """
    with open(file_path, encoding="utf-8") as file:
        data = file.readline().strip()
    return data


def get_tuple_of_numbers(data: str) -> tuple:
    """
    Преобразует строку, разделенную пробелами, в список чисел.
    :param data: строка в формате "3 89 56 7".
    :return: список чисел или None если преобразование не удалось.
    """
    tuple_of_numbers = None
    try:
        tuple_of_numbers = tuple(int(i) for i in data.split())
    except ValueError:
        print("File data is not correct")
    return tuple_of_numbers


def _min(data: tuple) -> int:
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


def _max(data: tuple) -> int:
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


def _sum(data: tuple) -> int:
    """
    Суммирует элементы кортежа.
    :param data: кортеж, где все элементы числа.
    :return: число - сумму всех элементов.
    """
    result = 0
    for item in data:
        result += item
    return result


def _mult(data: tuple) -> int:
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


def calculate_date_from_file(
        _file_path: str) -> tuple[int, int, int, int] | None:
    """
    Считывает из файла числа, и возвращает минимальное, максимальное число,
    их общую сумму и произведение.
    :param _file_path: путь к файлу.
    :return: кортеж из четырех чисел.
    """
    data_from_file = get_data_from_file(_file_path)
    nums = get_tuple_of_numbers(data_from_file)
    if nums is not None:
        return _min(nums), _max(nums), _sum(nums), _mult(nums)


if __name__ == '__main__':
    _FILE_PATH = "numbers.txt"
    min_, max_, sum_, mult_ = calculate_date_from_file(_FILE_PATH)
    print(
        f"Минимум: {min_}, максимум: {max_}, "
        f"сумма: {sum_}, произведение:{mult_}",
    )
