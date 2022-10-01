def quick_sort(arr: list):
    if len(arr) < 2:  # массивы с 0 или одним
        # элементом уже отсортированы
        return arr
    else:
        pivot = arr[0] # базовый элемент, относительно
        # которого будем делить массив
        greater_lst = [el for el in arr if el > pivot]
        less_lst = [el for el in arr if el < pivot]
        return quick_sort(less_lst) + [pivot] + quick_sort(greater_lst)


if __name__ == "__main__":
    print(quick_sort([1, 35, 89, 13, 45]))
