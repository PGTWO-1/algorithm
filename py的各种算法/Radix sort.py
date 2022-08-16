def radix_Sort(arr):
    n = len(str(max(arr)))
    for k in range(n):
        res = [[] for i in range(10)]
        for i in arr:
            res[i // (10 ** k) % 10].append(i)
        k = []
        for i in range(10):
            if res[i] is not None:
                for j in res[i]:
                    k.append(j)
        arr = k
    return arr


if __name__ == '__main__':
    arr = [132, 523, 4, 15, 34, 2, 6, 56, 3425]
    arr = radix_Sort(arr)
    print(arr)
