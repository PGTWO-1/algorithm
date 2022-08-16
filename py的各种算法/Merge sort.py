def mergesort(n, S):
    if n > 1:
        h = n // 2
        m = n - h
        U = []
        V = []
        for i in range(n):
            if i < h:
                U.append(S[i])
            else:
                V.append(S[i])
        mergesort(h, U)
        mergesort(m, V)
        merge(h, m, U, V, S)

    return S


def merge(h, m, U, V, S):
    i = 0
    j = 0
    k = 0
    while (i < h and j < m):
        if U[i] < V[j]:
            S[k] = U[i]
            i = i + 1
        else:
            S[k] = V[j]
            j = j + 1
        k = k + 1
    if i >= h:
        for p in range(k, h + m):
            S[p] = V[j]
            j = j + 1
    else:
        for p in range(k, h + m):
            S[p] = U[i]
            i = i + 1


if __name__ == '__main__':
    S = [1, 54, 7, 8, 98, 5, 4, 34, 7, 8, 6, 3]
    print(mergesort(len(S), S))
