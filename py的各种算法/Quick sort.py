def quick_sort(low, high, S):
    if high > low:
        pivot = partition(low, high, 0, S)
        quick_sort(low, pivot - 1,S)
        quick_sort(pivot + 1, high,S)
    return S


def partition(low, high, pivot, S):
    pivotitem = S[low]
    j = low
    for i in range(low + 1, high):
        if S[i] < pivotitem:
            j = j + 1
            S[i], S[j] = S[j], S[i]
    pivot = j
    S[low], S[pivot] = S[pivot], S[low]
    return pivot


if __name__ == '__main__':
    S = [1, 3, 46, 8, 34, 23, 465, 15, 7, 2, 345, 3]
    print(quick_sort(0, len(S), S))
