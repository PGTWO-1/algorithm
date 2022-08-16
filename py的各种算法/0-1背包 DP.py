def knapsack(v, w, W):
    n = len(v)
    k = [[0 for i in range(W+1)] for j in range(n)]

    for i in range(n):
        for j in range(W+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            else:
                k[i][j] = k[i - 1][j]
                if j >= w[i]:
                    k[i][j] = max(k[i - 1][j], k[i - 1][j - w[i]] + v[i])
    return k


if __name__ == '__main__':
    v = [0,10, 12, 15, 20]
    w = [0,1, 1, 2, 3]
    W = 5
    k=knapsack(v, w, W)
    print(k)