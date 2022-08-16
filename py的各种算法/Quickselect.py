def selection(low, high, S, k):
    if low == high:
        return S[low]
    else:
        pivotpoint = partition(low, high, S)
        if k == pivotpoint:
            return S[pivotpoint]
        else:
            if k < pivotpoint:
                return selection(low, pivotpoint - 1, S, k)
            else:
                selection(pivotpoint + 1, high, S, k)
    return S[k]


def partition(low, high, S):
    pivotitem = S[low]
    j = low
    for i in range(low + 1, high):
        if S[i] < pivotitem:
            j = j + 1
            S[i], S[j] = S[j], S[i]
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    return pivotpoint


if __name__ == '__main__':
    S = [1, 3, 46, 8, 34, 23, 465, 15, 7, 2, 345, 3]
    k = int(input("Please input the index of array: "))
    res = selection(0, len(S), S, k)
    print(S, res)
