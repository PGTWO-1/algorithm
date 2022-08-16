import sys


def chained_mat_mult(n, D):
    M = [[0 for i in range(n + 1)] for j in range(n + 1)]
    P = [[0 for i in range(n + 1)] for j in range(n + 1)]
    mininum = sys.maxsize
    for l in range(1, n):
        for i in range(1, n - l + 1):
            j = i  + l
            for k in range(i, j):
                if mininum >= M[i][k] + M[k + 1][j] + D[i - 1] * D[k] * D[j]:
                    mininum= M[i][k] + M[k + 1][j] + D[i - 1] * D[k] * D[j]
                    count=k
            M[i][j]=mininum
            P[i][j]=count
    return M,P


if __name__ == '__main__':
    D = [30, 35, 15, 5, 10, 20, 25]
    n = 6
    arr, P=chained_mat_mult(n, D)
    print(arr[1][n]," ",P[1][n])
