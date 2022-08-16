def bin_coef_dp(n, k):
    B = [[0 for i in range(n+1)] for j in range(k+1)]
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i - 1][j - 1] + B[i - 1][j]
    return B


if __name__ == '__main__':
    arr = bin_coef_dp(5, 5)
    print(arr)
