def find_smallest(arr: list) -> int:
    """
    Возвращает индекс наименьшего элемента списка
    :param arr: список анализируемых значений
    :return: индекс наименьшего значения
    """
    smallest_el = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest_el:
            smallest_el = arr[i]
            smallest_index = i
    return smallest_index


def sort_by_selection(arr: list) -> list:
    """
    Сортирует массив, использую алгоритм
    сортировки выбоором O(n*n)
    :param arr: массив чисел
    :return: отсортированный по возрастанию массив
    """
    sorted_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr



if __name__ == "__main__":
    print(find_smallest([1, 34, 15, 0]))
    print(sort_by_selection([12, 5, 78, 17]))
