def heap_ify(array, n, i):
    largest = i
    l = 2 * i + 1  # 左边的元素
    r = 2 * i + 2  # 右边的元素
    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heap_ify(array, n, largest)


def heap_sort(array):
    n = len(array)
    for i in range(n, -1, -1):
        heap_ify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heap_ify(array, i, 0)


arr = [1, 6, 8, 10, 2, 15, 7, 9, 5, 3]
heap_sort(arr)
print(arr)
