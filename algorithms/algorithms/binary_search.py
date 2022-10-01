def binary_search(test_list: list, item: int) -> int:
    """
    Осуществляет поиск элемента в списке,
    используя алгоритм бинарного поиска O(logn)
    :param test_list: список элементов (чисел)
    :param item: элемент (число)
    :return: индекс элемента в списке
    """
    low_index = 0  # нижняя граница диапазона поиска
    high_index = len(test_list) - 1  # верхняя граница диапазона поиска

    while low_index <= high_index:
        mid = int((low_index + high_index) / 2)
        guess = test_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high_index = mid - 1
        else:
            low_index = mid + 1
    return None


if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 3))
    print(binary_search(my_list, 9))
