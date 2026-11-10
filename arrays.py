MAX_SIZE = 100


def validate_array(arr: list) -> None:
    """Проверяет корректность входного массива.

    Raises:
        TypeError: если arr не список или элемент не является символом.
        ValueError: если массив длиннее 100 элементов или содержит
                    не латинские буквы.
    """
    if not isinstance(arr, list):
        raise TypeError("Массив должен быть списком")
    if len(arr) > MAX_SIZE:
        raise ValueError(f"Размер массива не должен превышать {MAX_SIZE}")
    for c in arr:
        if not isinstance(c, str) or len(c) != 1:
            raise TypeError("Элемент массива должен быть одним символом")
        if not ('a' <= c <= 'z' or 'A' <= c <= 'Z'):
            raise ValueError(f"Недопустимый символ: {c!r}. Разрешены только латинские буквы")


def is_lowercase_sorted(arr: list) -> bool:
    """Процедура проверки: строчные буквы массива идут в алфавитном порядке.

    Заглавные буквы игнорируются. Повторы допускаются (a, a, b).
    В процедуру передаются все элементы массива.
    """
    validate_array(arr)
    lowercase = [c for c in arr if 'a' <= c <= 'z']
    return all(lowercase[i] <= lowercase[i + 1] for i in range(len(lowercase) - 1))


def main() -> None:
    arrays = [
        ['a', 'B', 'c', 'D', 'e'],
        ['z', 'a', 'b'],
        ['A', 'B', 'C'],
        ['a', 'a', 'b', 'x'],
        ['m', 'k', 'Z'],
    ]

    for number, arr in enumerate(arrays, start=1):
        try:
            if is_lowercase_sorted(arr):
                print(f"Массив {number}: строчные буквы в алфавитном порядке, номер = {number}")
            else:
                print(f"Массив {number}: нет (-1)")
        except (TypeError, ValueError) as error:
            print(f"Массив {number}: ошибка данных - {error}")


if __name__ == "__main__":
    main()
