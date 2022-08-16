def heapify(arr, n, i):
    r = 2 * i + 1
    l = 2 * i
    if l < n and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest is not i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def build_max_heaps(arr, n):
    i = n // 2
    while i >= 0:
        heapify(arr, n, i)
        i -= 1
def heapSort(arr):
    n = len(arr)
    build_max_heaps(arr, n)
    for k in range(n - 1, 0, -1):
        arr[k], arr[0] = arr[0], arr[k]
        heapify(arr, k, 0)
if __name__ == '__main__':
    arr = [13, 11, 12, 5, 6, 7]
    heapSort(arr)
    n = len(arr)
    print("Sorted array is",arr)

