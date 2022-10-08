def get_data_from_file(file_path: str) -> str:
    with open(file_path) as file:
        data = file.readline().strip()
    return data


def get_tuple_of_numbers(data: str) -> tuple[int]:
    tuple_of_numbers = None
    try:
        tuple_of_numbers = tuple(int(i) for i in data.split())
    except ValueError as e:
        print("File data is not correct")
    return tuple_of_numbers


def _min(data: tuple[int]) -> int:
    result = data[0]
    for i in range(1, len(data)):
        if data[i] < result:
            result = data[i]
    return result


def _max(data: tuple[int]) -> int:
    result = data[0]
    for i in range(1, len(data)):
        if data[i] > result:
            result = data[i]
    return result


def _sum(data: tuple[int]) -> int:
    result = 0
    for item in data:
        result += item
    return result


def _mult(data: tuple[int]) -> int:
    result = None
    for item in data:
        if result is None:
            result = item
        else:
            result *= item
    return result


def main():
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
