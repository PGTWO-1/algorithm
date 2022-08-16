def partition_Decision(i, weight, remain, w, n):
    if weight == remain:
        print("Yes",weight,remain)
    else:
        if i < n - 1:
            partition_Decision(i + 1, weight + w[i + 1], remain - w[i + 1], w, n)
            partition_Decision(i + 1, weight, remain, w, n)


if __name__ == '__main__':
    res = []
    w = [3, 4, 5, 6]
    n = len(w)
    remain = 0
    for i in w:
        remain += i
    remain -= w[0]
    print(remain)
    partition_Decision(0, w[0], remain, w, n)
